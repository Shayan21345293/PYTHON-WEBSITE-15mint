import streamlit as st

st.set_page_config(page_title="Shayan Ali | My App", page_icon="🖥️") 
st.title("WELCOME TO MY PYTHON WEBSITE😉")
st.header("This my  simple streamlit app build in just 15 minutes ⌚")
name =st.text_input("Enter your name:", "Shayan Ali")
if st.button("Click me!👆"):
    st.write(f"Thank you for clicking me😀,{name}")