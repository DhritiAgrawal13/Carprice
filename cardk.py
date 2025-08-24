import streamlit as st
import pickle
import numpy as np

# Load trained RandomForest model
with open("name.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Car Price Prediction App 🚗")

st.write("Enter the car details to predict its Selling Price:")

# Numeric Inputs
year = st.number_input("Year", min_value=1990, max_value=2025, step=1)
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, step=0.1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, step=500)
owner = st.number_input("Number of Previous Owners", min_value=0, max_value=5, step=1)

# Dropdown Inputs for categorical columns
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Other"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual", "Other"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic", "Other"])

# Encoding (same as LabelEncoder used in notebook)
if fuel_type == "Petrol":
    fuel_val = 2
elif fuel_type == "Diesel":
    fuel_val = 1
elif fuel_type == "CNG":
    fuel_val = 0
else:
    fuel_val = -1

if seller_type == "Dealer":
    seller_val = 0
elif seller_type == "Individual":
    seller_val = 1
else:
    seller_val = -1

if transmission == "Manual":
    trans_val = 1
elif transmission == "Automatic":
    trans_val = 0
else:
    trans_val = -1

# Prepare features in exact same order as training
features = np.array([[year, present_price, kms_driven, fuel_val, seller_val, trans_val, owner]])

if st.button("Predict"):
    if -1 in [fuel_val, seller_val, trans_val]:
        st.error(" Unsupported category selected. Please choose valid options.")
    else:
        prediction = model.predict(features)
        st.success(f" Predicted Selling Price: {prediction[0]:.2f} lakhs")
