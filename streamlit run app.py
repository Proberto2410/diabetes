import os

# Caminho relativo para o seu script Streamlit
script_path = os.path.join(os.path.dirname(__file__), 'model_fhs.py')

# Comando para executar o script Streamlit
os.system(f'streamlit run{script_path}')