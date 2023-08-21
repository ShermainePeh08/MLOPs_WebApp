import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model
from pathlib import Path


st.title('Medical Prediction')

def predict_disease(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    # print(predictions_data['prediction_label'])
    return predictions_data['prediction_label'][0]
    
model = load_model(Path(__file__).parents[1] / 'medical_pipeline')

def get_user_input():
    st.write("Please fill in the required information to get your prediction :D")

    # Age
    age = st.slider("Age", 0, 120, step=1)

    # Gender
    gender = st.radio("Gender", ("M", "F"))
    
    # Fasting Blood Sugar
    fasting_BS = st.radio("Fasting Blood Sugar (Normal less than 100mg/dL for non-diabetes and 100-125mg/dL for diabetes)", ("Y", "N"))
    
    # Exercise Induced Angina
    exercise_angina = st.radio("Exercise Induced Angina", ("No", "Yes"))

    # Resting Blood Pressure
    resting_BP = st.number_input("Resting Blood Pressure", 80)

    # Cholesterol
    cholesterol = st.number_input("Cholesterol (mg/dl)", 100)

    # Old Peak
    old_peak = st.number_input("Old Peak", 0.0)
    
    # Maximum Heart Rate Achieved
    max_HR = st.slider("Max Heart Rate Achieved", 60, 202)
    
    # Resting ECG
    resting_ECG_options = ["Normal", "LVH", "ST"]
    resting_ECG = st.selectbox("Resting Electrocardiographic Results", resting_ECG_options)

    # Chest Pain
    chest_pain_options = ["ATA", "NAP", "ASY", "TA"]
    chest_pain = st.selectbox("Chest Pain Type", chest_pain_options)
    
    # ST Slope
    ST_slope_options = ["Up", "Flat", "Down"]
    ST_slope = st.selectbox("ST Slope", ST_slope_options)

    user_input = {
        "age": age,
        "gender": gender,
        "chest_pain": chest_pain,
        "resting_BP": resting_BP,
        "cholesterol": cholesterol,
        "fasting_BS": 1 if fasting_BS else 0,
        "resting_ECG": resting_ECG,
        "max_HR": max_HR,
        "exercise_angina": 1 if exercise_angina else 0,
        "old_peak": old_peak,
        "ST_slope": ST_slope,
    }

    features_df = pd.DataFrame([user_input])
    # prediction = predict_quality(model, features_df)
    # st.write(prediction)
    return features_df, user_input



if __name__ == "__main__":
    col1, col2, col3 = st.columns([3, 1, 2])
    with col1:
        df, user_input = get_user_input()
    with col3:
        prediction = predict_disease(model, df)
        st.subheader('Predicted Output')
        # st.table(user_input)
        if prediction == 1:
            st.markdown("<h1 style='color: red;'>‼️ OH NO ‼️</h1>", unsafe_allow_html=True)
            st.write(f':red[Based on feature values, you are likely to have cardiovascular issues]')
        if prediction == 0:
            st.markdown("<h1 style='color: green;'>YAY 😀</h1>", unsafe_allow_html=True)
            st.write(f':green[Based on feature values, you are normal. Unlikely to have cardiovascular issues]')