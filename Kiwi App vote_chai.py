import streamlit as st

st.title("Chai Voting Dashboard")
st.header("Vote the Tasty Chai")
col1,col2 = st.columns(2)
with col1:
  st.header("Masala Chai☕")
  vote1 = st.button("Vote Masala chai")

with col2:
  st.header("Adrak Chai🍵")
  vote2 = st.button("Vote Adrak Chai")

if vote1:
  st.success("Thanks for voting Masala Chai🏆")

else:
  st.success("Thanks for voting Adrak Chai🏆")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai",["Masala","Ilaichi","Adrak"])
st.write(f"Welcome {name} to the Votiing Playground and your {tea} is getting ready!")

with st.expander("Show Chai Making Instructions--"):
  st.write('''
  1. Boil water
  2. Add Milk
  3. Add masala
  4. Serve hot tea
  ''')
st.markdown("## Have a nice day😊")
st.markdown("> Quote")






