# AI Introduction Project

Este é um projeto de introdução à Inteligência Artificial usando Python e Jupyter Notebook, focado em aprendizado de máquina e análise de dados.

## Estrutura do Projeto

```
.
├── ai-creating/
│   ├── ai-model.ipynb      # Notebook com modelo de previsão de preços de casas
│   └── requirements.txt    # Dependências do notebook
├── ai-applying/            # Diretório para aplicações práticas de IA
│   └── gptAPI.py           # Exemplo de uso da API do GPT
├── app.py                  # API Flask para o projeto
├── api-tests.http          # Testes de API usando REST Client
├── requirements.txt        # Dependências do projeto completo
├── LICENSE                 # Licença do projeto
└── README.md               # Este arquivo
```

## Sobre o Projeto

O projeto contém implementações práticas de IA, incluindo:

- Modelo de regressão linear para previsão de preços de casas na Califórnia
- Utilização do dataset California Housing do scikit-learn
- Pré-processamento de dados com StandardScaler
- Avaliação de modelo usando train-test split
- API REST para acesso às funcionalidades de IA
- Integração com a API do OpenAI GPT

## Requisitos

- Python 3.13.2
- Jupyter Notebook
- Principais dependências:
  - flask
  - pandas
  - scikit-learn
  - numpy
  - openai

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Natanaelvich/ai-for-devs_introduction.git
cd ai-for-devs_introduction
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv .venv
source .venv/bin/activate  # No Linux/Mac
# ou
.venv\Scripts\activate  # No Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com:
```
OPENAI_API_KEY=sua_chave_api_openai
```

## Uso

### Jupyter Notebook
1. Ative o ambiente virtual (se estiver usando)
2. Navegue até o diretório do projeto
3. Inicie o Jupyter Notebook:
```bash
jupyter notebook
```
4. Abra o notebook desejado:
   - `ai-creating/ai-model.ipynb` para o modelo de previsão de preços de casas

### API REST
1. Ative o ambiente virtual
2. Inicie o servidor Flask:
```bash
python app.py
```
3. O servidor estará disponível em `http://localhost:5000`

## API Endpoints

### Health Check
```
GET /api/health
```
Verifica o status da API e se o modelo está carregado.

### Treinar Modelo
```
POST /api/train
Content-Type: application/json
```
Treina o modelo de previsão de preços de casas usando o dataset California Housing.

### Prever Preço
```
POST /api/predict
Content-Type: application/json

{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984127,
    "AveBedrms": 1.023810,
    "Population": 322.0,
    "AveOccup": 2.555556,
    "Latitude": 37.88,
    "Longitude": -122.23
}
```
Faz uma previsão de preço de casa com base nos parâmetros fornecidos.

### Consultar GPT
```
POST /api/gpt
Content-Type: application/json

{
    "prompt": "Sua pergunta aqui",
    "system": "Instrução para o sistema (opcional)",
    "model": "Nome do modelo (opcional, padrão: gpt-4o-mini)"
}
```
Envia uma consulta para a API do OpenAI GPT e retorna a resposta.

## Testes da API

O projeto inclui um arquivo `api-tests.http` que pode ser usado com a extensão REST Client do VS Code para testar todos os endpoints da API.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes. 