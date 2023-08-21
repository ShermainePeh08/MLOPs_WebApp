import streamlit as st
import pandas as pd
from pycaret.regression import load_model as load_model_regression, predict_model as predict_model_regression
from pathlib import Path

st.title('HDB Prediction')

def predict_hdb(model, df):
    
    predictions_data = predict_model_regression(estimator = model, data = df)
    return predictions_data['prediction_label']
    
hdb_model = load_model_regression(Path(__file__).parents[1] / 'hdb_pipeline')

def get_user_input():
    st.write("Please fill in the required information to get your prediction :D")

    # Street Name
    street_name = st.text_input("Street Name", 'ANG MO KIO AVENUE 3')

    # Town
    towns = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN']
    town = st.selectbox("Town", towns)

    # Postal Code
    postal_code = st.number_input("Postal Code", 569830)

    # Month of Sale
    month = st.date_input("Month of Sale")

    # Flat Type
    flat_types = ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM', 'MULTI-GENERATION'] 
    flat_type = st.selectbox("Flat Type", flat_types)

    # Storey Range
    storey_ranges = ['01 TO 03', '04 TO 06', '07 TO 09', '10 TO 12','13 TO 15', '16 TO 18', '19 TO 21',  '22 TO 24', '25 TO 27', '28 TO 30', '31 TO 33', '34 TO 36', '37 TO 39', '40 TO 42', '43 TO 45', '46 TO 48', '49 TO 51'] 
    storey_range = st.selectbox("Storey Range", storey_ranges)

    # Floor Area
    floor_area_sqm = st.number_input("Floor Area (sqm)", 100)

    # Flat Model
    flat_models = ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified', 'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2', 'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS', 'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation', 'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen']
    flat_model = st.selectbox("Flat Model", flat_models)

    # Lease Commence Date
    lease_commence_date = st.slider("Lease Commence Year", 1965, 2020, step=1)

    # Latitude and Longitude 
    # latitude = st.number_input("Latitude", value=1.37, format="%.5f") 
    # longitude = st.number_input("Longitude", value=103.84, format="%.5f") 

    # CBD Distance and MRT Distance
    cbd_dist = st.number_input("Distance from CBD (m)", 10000)
    min_dist_mrt = st.number_input("Minimum Distance from MRT (m)", 10000)
    
    user_input = {
        "street_name": street_name,
        "town": town,
        "postal_code": postal_code,
        "month": month.strftime('%Y-%m'),
        "flat_type": flat_type,
        "storey_range": storey_range,
        "floor_area_sqm": floor_area_sqm,
        "flat_model": flat_model,
        "lease_commence_date": int(lease_commence_date), 
        'cbd_dist': cbd_dist, 
        'min_dist_mrt': min_dist_mrt,
    }

    features_df = pd.DataFrame([user_input])
    features_df['month'] = pd.to_datetime(features_df['month'])
    return features_df, user_input


if __name__ == "__main__":
    col1, col2, col3 = st.columns([3, 1, 2])
    with col1:
        df, user_input = get_user_input()
    with col3:
        prediction = predict_hdb(hdb_model, df)
        st.subheader('Predicted Output')
        st.write(prediction)
        # st.write('The predicted price of your HDB is: $', prediction, 'SGD')