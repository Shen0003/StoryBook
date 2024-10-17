import streamlit as st

#Set the app title
st.title('My first streamlit app')

#Display text output
st.write("Welcome to my first streamlist app")

#Display buttons
st.button("Reset", type="primary"
          )  ##Primary type button will reset the states of any other buttons

if st.button("Say Hello"):  ##Before the btn is clicked, the value is "else"
  st.write("Why hello there")
else:
  st.write("Goodbye")

#TO RUN APP: streamlit run [FILE NAME].py
#IF open too many port, go to 'networking' to remove.
