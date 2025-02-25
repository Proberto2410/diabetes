import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler

# No Streamlit app
model_path = os.path.join(os.path.dirname(__file__), 'notebooks', 'dia_RF_model.pkl')


try:
    model = joblib.load(model_path)
    
    st.success("Modelo e preprocessador carregados com sucesso.")
except Exception as e:
    st.error(f"Erro ao carregar: {e}")
    st.stop()