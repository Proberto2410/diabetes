# Heart Attack Prediction


465 / 5 000
This project predicts the probability of a heart attack in 10 years based on several health indicators.

## Project Structure

- `notebooks/heart_analysis.ipynb`: Notebook used to train the model.
- `models/fhs_rf_model.pkl`: Trained model saved.
- `src/streamlit_fhs.py`: Streamlit script for predictions.
- `run_streamlit.py`: Script to start Streamlit.
- `requirements.txt`: Dependencies file.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/seu-usuario/heart-attack-prediction.git
   cd heart-attack-prediction
 


2. Instale as dependências:
<pip install -r requirements.txt>

3. Inicie o aplicativo Streamlit:
<python run_streamlit.py>

4. Abra o navegador e acesse http://localhost:8501 para usar o aplicativo.

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

