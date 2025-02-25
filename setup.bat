@echo off
echo Setting up AI Introduction Project...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python and try again.
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed or not in PATH. Please install pip and try again.
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment. Please check your Python installation.
        exit /b 1
    )
    echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)
echo Virtual environment activated.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    exit /b 1
)
echo Dependencies installed successfully.

REM Check if .env file exists, if not create from example
if not exist .env (
    echo Creating .env file from .env.example...
    copy .env.example .env
    echo .env file created. Please edit it to add your OpenAI API key.
    echo IMPORTANT: You need to add your OpenAI API key to the .env file.
) else (
    echo .env file already exists.
)

echo Setup completed successfully!
echo To run the application:
echo 1. Make sure your virtual environment is activated: .venv\Scripts\activate
echo 2. Run the Flask application: python app.py
echo 3. Access the API at: http://localhost:5000
echo To deactivate the virtual environment when done: deactivate 