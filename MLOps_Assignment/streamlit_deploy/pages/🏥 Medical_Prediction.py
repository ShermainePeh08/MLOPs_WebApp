import streamlit as st
import pandas as pd
from streamlit_modal import Modal

st.title('Medical Prediction')

# def predict_quality(model, df):
    
#     predictions_data = predict_model(estimator = model, data = df)
#     return predictions_data['Label'][0]
    
# model = load_model('extra_tree_model')

def get_user_input():
    st.write("Please fill in the required information to get your prediction :D")

    # Age
    age = st.slider("Age", 0, 120, step=1)

    # Gender
    gender = st.radio("Gender", ("M", "F"))
    
    # Fasting Blood Sugar
    fasting_BS = st.radio("Fasting Blood Sugar", ("Y", "N"))
    
    # Exercise Induced Angina
    exercise_angina = st.radio("Exercise Induced Angina", ("No", "Yes"))

    # Resting Blood Pressure
    resting_BP = st.number_input("Resting Blood Pressure", 80)

    # Cholesterol
    cholesterol = st.number_input("Cholesterol (mg/dl)", 100)

    # Old Peak
    old_peak = st.number_input("Old Peak", 0.0)
    
    # Maximum Heart Rate Achieved
    max_HR = st.slider("Max Heart Rate Achieved", 60, 200)
    
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
    return features_df



if __name__ == "__main__":
    user_input = get_user_input()
    modal = Modal("Demo Modal", key = "demo")
    open_modal = st.button("Predict!")
    if open_modal:
        modal.open()

    if modal.is_open():
        with modal.container():
            st.table(user_input)  
            prediction = "predict"
            st.write(f'Based on feature values, your wine quality is {prediction}')