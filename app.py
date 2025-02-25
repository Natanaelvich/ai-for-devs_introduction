from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import joblib
import numpy as np
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client if API key is available
openai_api_key = os.getenv("OPENAI_API_KEY")
client = None
if openai_api_key and openai_api_key != "your_openai_api_key_here":
    client = OpenAI(api_key=openai_api_key)

# Load the model if it exists
MODEL_PATH = "model/housing_model.pkl"
SCALER_PATH = "model/scaler.pkl"

model = None
scaler = None

try:
    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
except Exception as e:
    print(f"Error loading model: {str(e)}")

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None and scaler is not None
    })

@app.route("/api/predict", methods=["POST"])
def predict_housing_price():
    try:
        if model is None or scaler is None:
            return jsonify({
                "error": "Model not loaded. Please train the model first."
            }), 500
            
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        # Expected features in the correct order
        required_features = [
            "MedInc", "HouseAge", "AveRooms", "AveBedrms", 
            "Population", "AveOccup", "Latitude", "Longitude"
        ]
        
        # Check if all required features are present
        for feature in required_features:
            if feature not in data:
                return jsonify({
                    "error": f"Missing required feature: {feature}"
                }), 400
                
        # Create feature array in the correct order
        features = np.array([[
            data["MedInc"], 
            data["HouseAge"], 
            data["AveRooms"], 
            data["AveBedrms"],
            data["Population"], 
            data["AveOccup"], 
            data["Latitude"], 
            data["Longitude"]
        ]])
        
        # Scale features
        scaled_features = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(scaled_features)
        
        return jsonify({
            "prediction": prediction[0] * 100000,  # Convert to actual price in dollars
            "features": data
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/train", methods=["POST"])
def train_model():
    try:
        from sklearn.datasets import fetch_california_housing
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.preprocessing import StandardScaler
        import os
        
        # Create model directory if it doesn't exist
        os.makedirs("model", exist_ok=True)
        
        # Load California housing dataset
        housing = fetch_california_housing()
        X = housing.data
        y = housing.target
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale the features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Train the model
        model = LinearRegression()
        model.fit(X_train_scaled, y_train)
        
        # Evaluate the model
        train_score = model.score(X_train_scaled, y_train)
        test_score = model.score(X_test_scaled, y_test)
        
        # Save the model and scaler
        joblib.dump(model, MODEL_PATH)
        joblib.dump(scaler, SCALER_PATH)
        
        # Update the global model and scaler
        globals()["model"] = model
        globals()["scaler"] = scaler
        
        return jsonify({
            "message": "Model trained and saved successfully",
            "train_score": train_score,
            "test_score": test_score,
            "feature_names": housing.feature_names
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/gpt", methods=["POST"])
def query_gpt():
    try:
        if client is None:
            return jsonify({
                "error": "OpenAI API key not configured. Please set the OPENAI_API_KEY environment variable."
            }), 500
            
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Missing 'prompt' in request body"}), 400
            
        prompt = data["prompt"]
        system_message = data.get("system", "You are a helpful assistant.")
        model_name = data.get("model", "gpt-4o-mini")
        
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        
        return jsonify({
            "response": completion.choices[0].message.content,
            "model": model_name
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000) 