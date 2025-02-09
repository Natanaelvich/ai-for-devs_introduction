# AI Introduction Project

Este é um projeto de introdução à Inteligência Artificial usando Python e Jupyter Notebook, focado em aprendizado de máquina e análise de dados.

## Estrutura do Projeto

```
.
├── ai-creating/
│   ├── ai-model.ipynb      # Notebook com modelo de previsão de preços de casas
│   └── requirements.txt    # Dependências do projeto
├── ai-applying/            # Diretório para aplicações práticas de IA
├── LICENSE                 # Licença do projeto
└── README.md              # Este arquivo
```

## Sobre o Projeto

O projeto contém implementações práticas de IA, incluindo:

- Modelo de regressão linear para previsão de preços de casas na Califórnia
- Utilização do dataset California Housing do scikit-learn
- Pré-processamento de dados com StandardScaler
- Avaliação de modelo usando train-test split

## Requisitos

- Python 3.13.2
- Jupyter Notebook
- Principais dependências:
  - pandas
  - scikit-learn
  - numpy

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
pip install -r ai-creating/requirements.txt
```

## Uso

1. Ative o ambiente virtual (se estiver usando)
2. Navegue até o diretório do projeto
3. Inicie o Jupyter Notebook:
```bash
jupyter notebook
```
4. Abra o notebook desejado:
   - `ai-creating/ai-model.ipynb` para o modelo de previsão de preços de casas

## Funcionalidades

### Modelo de Previsão de Preços de Casas
- Dataset: California Housing
- Features incluem:
  - MedInc (renda média)
  - HouseAge (idade da casa)
  - AveRooms (média de quartos)
  - AveBedrms (média de dormitórios)
  - Population (população)
  - AveOccup (média de ocupantes)
  - Latitude
  - Longitude

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes. 