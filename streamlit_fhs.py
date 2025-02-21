import streamlit as st
import joblib
import pandas as pd
import os

# Título da aplicação
st.write("# 10 Year Heart Disease Prediction")

# Layout com colunas
col1, col2, col3 = st.columns(3)

# Entradas do usuário
gender = col1.selectbox("Enter your gender", ["Male", "Female"])
age = col2.number_input("Enter your age", min_value=0, max_value=120, value=30)
education = col3.selectbox("Highest academic qualification", ["High school diploma", "Undergraduate degree", "Postgraduate degree", "PhD"])
isSmoker = col1.selectbox("Are you currently a smoker?", ["Yes", "No"])
yearsSmoking = col2.number_input("Number of daily cigarettes", min_value=0, value=0)
BPMeds = col3.selectbox("Are you currently on BP medication?", ["Yes", "No"])
stroke = col1.selectbox("Have you ever experienced a stroke?", ["Yes", "No"])
hyp = col2.selectbox("Do you have hypertension?", ["Yes", "No"])
diabetes = col3.selectbox("Do you have diabetes?", ["Yes", "No"])
chol = col1.number_input("Enter your cholesterol level", min_value=0, value=200)
sys_bp = col2.number_input("Enter your systolic blood pressure", min_value=0, value=120)
dia_bp = col3.number_input("Enter your diastolic blood pressure", min_value=0, value=80)
bmi = col1.number_input("Enter your BMI", min_value=0.0, value=25.0)
heart_rate = col2.number_input("Enter your resting heart rate", min_value=0, value=70)
glucose = col3.number_input("Enter your glucose level", min_value=0, value=100)

# Botão de previsão
if st.button('Predict'):
    # Transformando as entradas do usuário em um DataFrame
    df_pred = pd.DataFrame([[gender, age, education, isSmoker, yearsSmoking, BPMeds, stroke, hyp, diabetes, chol, sys_bp, dia_bp, bmi, heart_rate, glucose]],
                           columns=['gender', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'])

    # Codificação das variáveis categóricas
    df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == 'Male' else 0)
    df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['currentSmoker'] = df_pred['currentSmoker'].apply(lambda x: 1 if x == 'Yes' else 0)

    def transform_education(data):
        if data == 'High school diploma':
            return 0
        elif data == 'Undergraduate degree':
            return 1
        elif data == 'Postgraduate degree':
            return 2
        elif data == 'PhD':
            return 3
        else:
            return 3  # Valor padrão

    df_pred['education'] = df_pred['education'].apply(transform_education)

    # Carregando o modelo
    model_path = os.path.join(os.path.dirname(__file__), 'notebooks', 'fhs_rf_model.pkl')
    try:
        model = joblib.load(model_path)
        st.success("")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

    # Fazendo a previsão
    prediction = model.predict(df_pred)

    # Exibindo o resultado
    if prediction[0] == 0:
        st.markdown('<p class="big-font">You likely will not develop heart disease in 10 years.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="big-font">You are likely to develop heart disease in 10 years.</p>', unsafe_allow_html=True)

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