# Heart Attack Prediction

Este projeto prevê a probabilidade de um ataque cardíaco em 10 anos com base em vários indicadores de saúde.

## Estrutura do Projeto

- `notebooks/heart_analysis.ipynb`: Notebook usado para treinar o modelo.
- `models/fhs_rf_model.pkl`: Modelo treinado salvo.
- `src/streamlit_fhs.py`: Script Streamlit para previsões.
- `run_streamlit.py`: Script para iniciar o Streamlit.
- `requirements.txt`: Arquivo de dependências.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/heart-attack-prediction.git
   cd heart-attack-prediction
 
 2. Instale as dependências:
 pip install -r requirements.txt

 3. Inicie o aplicativo Streamlit:
 python run_streamlit.py

 4. Abra o navegador e acesse http://localhost:8501 para usar o aplicativo.

Estrutura do Projeto

heart-attack-prediction/
├── notebooks/
│   └── heart_analysis.ipynb  # Notebook usado para treinar o modelo
├── models/
│   └── fhs_rf_model.pkl      # Modelo treinado salvo
├── src/
│   └── streamlit_fhs.py      # Script Streamlit para previsões
├── run_streamlit.py          # Script para iniciar o Streamlit
├── requirements.txt          # Arquivo de dependências
└── README.md                 # Documentação do projeto

