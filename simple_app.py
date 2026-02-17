import streamlit as st

st.title("📚 Personal Research Assistant")
st.write("Testing if basic UI works")

uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])

if uploaded_file:
    st.success("File uploaded!")
    
if st.button("Test Button"):
    st.write("Button works!")