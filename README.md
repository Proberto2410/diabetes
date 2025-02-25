# Diabetes Prediction Project

The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information.

## Features

- **Gender**: The biological sex of the individual, which can have an impact on their susceptibility to diabetes.
- **Age**: An important factor as diabetes is more commonly diagnosed in older adults.
- **Hypertension**: A medical condition in which the blood pressure in the arteries is persistently elevated.
- **Heart Disease**: A medical condition that is associated with an increased risk of developing diabetes.
- **Smoking History**: A risk factor for diabetes and can exacerbate the complications associated with it.
- **BMI (Body Mass Index)**: A measure of body fat based on weight and height.
- **HbA1c (Hemoglobin A1c)**: A measure of a person's average blood sugar level over the past 2-3 months.
- **Blood Glucose Level**: Refers to the amount of glucose in the bloodstream at a given time. High blood glucose levels can indicate diabetes.

## Target Variable

- **Diabetes**: The target variable being predicted. `1` indicates a positive diagnosis for diabetes, and `0` indicates a negative diagnosis.

## Running the Application

To run the Streamlit application, first install the required dependencies using the following command:

```sh
pip install -r requirements.txt
streamlit run model_dia.py

