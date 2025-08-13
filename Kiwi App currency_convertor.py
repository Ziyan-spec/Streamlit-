import streamlit as st
import requests

st.title("Currency Converter App")
amount = st.number_input("Enter amount in INR:", min_value=0.0)
target_currency = st.selectbox("Convert to: ", ["USD","JPY"])

if st.button("Convert"):
  url = "https://api.frankfurter.app/latest?amount=1&from=INR&to=USD"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    rate = data["rates"][target_currency]
    converted = rate*amount 
    st.success(f"{amount} INR = {converted: .2f} {target_currency}")
  else:
    st.error("Failed to fetch conversion rate")  
  






