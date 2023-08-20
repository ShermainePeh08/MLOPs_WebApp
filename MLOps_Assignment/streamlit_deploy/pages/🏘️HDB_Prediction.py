import streamlit as st
import streamlit as st
import pandas as pd

st.title('HDB Prediction')

# def predict_quality(model, df):
    
#     predictions_data = predict_model(estimator = model, data = df)
#     return predictions_data['Label'][0]
    
# model = load_model('extra_tree_model')

def get_user_input():
    st.write("Please fill in the required information to get your prediction :D")
    
    # Block
    block = st.text_input("Block Number")

    # Street Name
    street_name = st.text_input("Street Name")

    # Town
    towns = ["ANG MO KIO", "BEDOK", "BUKIT BATOK"]
    town = st.selectbox("Town", towns)

    # Postal Code
    postal_code = st.text_input("Postal Code")

    # Month of Sale
    month = st.date_input("Month of Sale")

    # Flat Type
    flat_types = ["3 ROOM", "4 ROOM", "5 ROOM", ...] 
    flat_type = st.selectbox("Flat Type", flat_types)

    # Storey Range
    storey_ranges = ["01 TO 03", "04 TO 06", "07 TO 09"] 
    storey_range = st.selectbox("Storey Range", storey_ranges)

    # Floor Area
    floor_area_sqm = st.number_input("Floor Area (sqm)")

    # Flat Model
    flat_models = ["Improved", "New Generation"]
    flat_model = st.selectbox("Flat Model", flat_models)

    # Lease Commence Date
    lease_commence_date = st.date_input("Lease Commence Date")

    # Latitude and Longitude 
    # latitude = st.number_input("Latitude", value=1.37, format="%.5f") 
    # longitude = st.number_input("Longitude", value=103.84, format="%.5f") 

    # CBD Distance and MRT Distance
    cbd_dist = st.number_input("Distance from CBD")
    min_dist_mrt = st.number_input("Minimum Distance from MRT")
    
    user_input = {
        "block": block,
        "street_name": street_name,
        "town": town,
        "postal_code": postal_code,
        "month": month.strftime('%Y-%m'),
        "flat_type": flat_type,
        "storey_range": storey_range,
        "floor_area_sqm": floor_area_sqm,
        "flat_model": flat_model,
        "lease_commence_date": lease_commence_date.year, 
    }

    features_df = pd.DataFrame([user_input])
    return features_df



if __name__ == "__main__":
    user_input = get_user_input()
    # if st.button('Predict'):
        # st.table(user_input)  
    #     prediction = "predict"
    #     st.write(' Based on feature values, your wine quality is '+ str(prediction))
