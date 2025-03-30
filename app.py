import streamlit as stm
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

stm.title('Placement hoga ya ni btane wale baba ji')

# Take user input
input_cgpa = stm.text_input("Enter your CGPA")
input_iq = stm.text_input("Enter your IQ")


if stm.button('Predict'):
    if input_cgpa == "" or input_iq == "":
        stm.header("Input box is empty")
    else:
        try:
            # Convert input to float
            input_cgpa = float(input_cgpa)
            input_iq = float(input_iq)
            # Predict
            result = model.predict(input_features)[0]
            # Display result
            if result == 1:
                stm.header("Ho jayega ✅")
            else:
                stm.header("Nhi Hoga ❌")
        except ValueError:
            stm.header("Please enter valid numeric values!")
