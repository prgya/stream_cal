import streamlit as st
import time
import requests
import json

st.title("hello world, lets calculate :tada:")

st.write("select your numbers")
operation = st.selectbox("what do you want to do ?", ("addition", "subtraction"))
x = st.slider("x", 0, 100, 20) # name to be displayed, start value, end value, default value
y = st.slider("y", 0, 100, 20)

print(operation, x)
calculator_url = 'http://127.0.0.1:8080/calculate'

inputs = {'operation': operation, 'a': x, 'b': y}
if st.button('Calculate'):
    st.write("calculating ...")
    time.sleep(2)
    res = requests.post(calculator_url, data=json.dumps(inputs))
    st.subheader(f"{operation} of {x} and {y} is {res.text} :tada:")

