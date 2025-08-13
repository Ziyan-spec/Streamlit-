import streamlit as st
st.title("Programming Languages App")
st.subheader("Brewed the Streamlit")
st.text("Building and Interactive App")
st.write("Select Your Language You Enjoy!!")
lang = st.selectbox("Select Your Favourite Language:",["Python","Javascript","C++","Java","Rust"])
st.write(f"You choose {lang}, Great Choice!!")
st.success("Congratulations, You Brewed Language.")
