import streamlit as stm
import pickle
model = pickle.load(open('model.pkl', 'rb'))

stm.title('Placement hoga ya ni btane wale baba ji')

input_cgpa = stm.text_area("Enter your CGPA")
input_iq = stm.text_area("Enter your IQ")

if stm.button('predict'):
  if (input_cgpa == "" or input_iq == ""):
    stm.header("input box is empty")
  else:
    result = model.predict(input_cgpa, input_iq)[0]
    # display
    if result == 1:
      stm.header("Ho jayega")
    else:
      stm.header("Nhi Hoga")