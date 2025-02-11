import streamlit as st
import pickle
import pandas as pd

st.title('Car Price Prediction using Linear Regression')
st.write('This web app predicts the **Car price**')

# To read the model from the pickle file
model=pickle.load(open('model_lr_car.pkl','rb'))

# get the input from the user

selling_price=st.number_input('Selling Price')
year=st.number_input('year')
km_driven=st.number_input('Km Driven')
fuel=st.number_input('Fuel')
seller_type=st.number_input('Seller Type')
transmission=st.number_input('Transmission')
owner=st.number_input('Owner')
mileage=st.number_input('Mileage_km/ltr/kg')
engine=st.number_input('Engine')
max_power=st.number_input('Max power')
seats=st.number_input('Seats')

# Convert the user input to a dataframe
user_data=pd.DataFrame({'Selling_price':selling_price,
                        'year':year,
                        'Km_driven':km_driven,
                        'Fuel':fuel,
                        'Seller_Type':seller_type,
                        'Owner':owner,
                        'Mileage':mileage,
                        'Engine':engine,
                        'Max power':max_power,
                        'Seats':seats}, index=[0])


#predict the house price
prediction=model.predict(user_data)
if st.button('Predict'):
    st.write(f'The predicted car price is {prediction[0]*1000000}')





