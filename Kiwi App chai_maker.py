import streamlit as st
st.title("Chai Maker App")
if st.button("Make Chai"):
  st.success("Your chai is ready!")

chai_masala = st.checkbox("Add Masala")
if chai_masala:
  st.write("Chai Masala Added..")

base_type = st.radio("Select your base:",["Water","Milk","Malai Milk"])
st.write(f"Selected based is {base_type}")

flavour = st.selectbox("Choose a flavour:", ["Adrak","Ilaichi","Lemon"])
st.write(f"Selected flavour is {flavour}")

sugar = st.slider("Select Sugar Level:",0,5,2)
st.write(f"Selected sugar level is {sugar}")

cups = st.number_input("Select Number of Cups:", min_value=1, max_value=10)
st.write(f"You selected {cups} cups of chai")

name = st.text_input("Enter your name:")
st.write(f"Hey {name}, your chai is on the way!")

dob = st.date_input("Enter your date of birth:")
st.write(f"Thnx {name} for sharing your date of birth, you are {dob}")






