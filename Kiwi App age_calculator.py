import streamlit as st
from datetime import date

st.title("AGE CALCULATOR")
dob = st.date_input("Enter your date of birth:")
today = date.today()
if(dob > today):
  st.error("Date of Birth can't be in the future!")
else:
  age = today.year - dob.year -((today.month,today.day) < (dob.month,dob.day))
  st.success(f"Your age is {age}")

  st.success("Congratulations 🎊, you have successfully calculated the age!!")