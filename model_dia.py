import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler

# Título da aplicação
st.write("# Diabetes Prediction")

# Layout com colunas
col1, col2 = st.columns(2)

# Entradas do usuário
age = col1.number_input("Enter your age/Informe sua idade", min_value=0)
gender = col1.selectbox("Enter your gender/Informe seu sexo", ["Male", "Female"])
hypertension = col1.selectbox("Hypertension/Hipertensão?", ['Yes', 'No'])
heart_disease = col1.selectbox("Heart Disease/Doença Cardíaca?", ['Yes', 'No'])
smoking_history = col2.selectbox("Smoking History/Já fumou?", ['never', 'No Info', 'former','current', 'not current', 'ever'])
bmi = col2.number_input("Enter your BMI/Peso dividido Altura²(m))", min_value=0.0)
HbA1c_level = col2.number_input("Enter your HbA1c/Hemoglobina Glicada", min_value=0.0)
blood_glucose_level = col2.number_input("Enter your Blood Glucose/Nível de Glicemia", min_value=0.0)

# Carregando o modelo e o preprocessador antecipadamente para verificar se estão disponíveis
model_path = os.path.join(os.path.dirname(__file__), 'notebooks', 'dia_RF_model.pkl')

# Tente carregar os arquivos no início para exibir mensagens de erro se necessário
try:
    model = joblib.load(model_path)
    st.success("Modelo e preprocessador carregados com sucesso!")
except Exception as e:
    st.error(f"Erro ao carregar arquivos: {e}")
    # Não use st.stop() aqui, pois impediria a exibição da interface

# Botão de previsão
if st.button('Predict'):
    # Transformando as entradas do usuário em um DataFrame
    df_pred = pd.DataFrame([[age, gender, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]],
                           columns=['age', 'gender', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level'])
    
    # Codificação das variáveis categóricas
    df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == 'Male' else 0)
    df_pred['hypertension'] = df_pred['hypertension'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['heart_disease'] = df_pred['heart_disease'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    def transform_smoking_history(data):
        if data == 'never':
            return 0
        elif data == 'No Info':
            return 1
        elif data == 'former':
            return 2
        elif data == 'current':
            return 3
        elif data == 'not current':
            return 4
        elif data == 'ever':
            return 5
        else:
            return 1  # Valor padrão
    
    df_pred['smoking_history'] = df_pred['smoking_history'].apply(transform_smoking_history)
    
    # Verificando os dados de entrada
    st.write("Dados de entrada:")
    st.write(df_pred)
    
    try:
        # Fazer a previsão
        prediction = model.predict(df_pred)
        
        # Exibir a previsão
        st.write("Previsão:")
        st.write(prediction)
        
        # Exibir o resultado de forma amigável
        if prediction[0] == 0:
            st.markdown('<p class="big-font">You likely WILL NOT develop Diabetes.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="big-font">You are likely to develop Diabetes.</p>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Erro ao processar: {e}")
        import traceback
        st.error(traceback.format_exc())

# Estilização personalizada
st.markdown("""
    <style>
    .big-font {
        font-size: 24px;
        color: #333;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)