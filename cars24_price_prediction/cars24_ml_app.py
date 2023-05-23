import pandas as pd 
import streamlit as st 
import yfinance as yf 
import datetime 
import pickle 


# cars_df = pd.read_csv("./cars24-car-price.csv")

st.write("This is cars24 used car price predictions")
# st.dataframe(cars_df.head())

encode_feature_values = {
    "fuel_type": {"Diesel":1, "Petrol":2, "CNG":3, "LPG":4, "Electric":5},
    "seller_type": {"Dealer":1, "Individual":2, "Trustmark Dealer":3},
    "transmission_type": {"Manual":1, "Automatic":2}
}

def model_pred(fuel_type, transmission_type, engine, seats):

    #loading the model 
    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file) 

    input_features = [[2018.0, 1, 40000, fuel_type, transmission_type, 19.70, engine, 86.34, seats]]
    return reg_model.predict(input_features)


col1, col2 = st.columns(2)
fuel_type = col1.selectbox("Select fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])  
engine = col1.slider("Set the engine power", 500, 5000, 100)

# seller_type = col2.selectbox("Select fuel type", ["Dealer", "Individual", "Trustmark Dealer"])
seats = col2.selectbox("No of Seats", [4, 5, 6, 7])    
transmission_type = col2.selectbox("Select fuel type", ["Manual", "Automatic"])


if st.button("Predicted Price"):
    fuel_type = encode_feature_values['fuel_type'][fuel_type]
    transmission_type = encode_feature_values['transmission_type'][transmission_type]

    price = model_pred(fuel_type, transmission_type, engine, seats)
    st.text("Predicted price of the car is: " + str(price))


















