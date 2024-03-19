import streamlit as st

st.title ("Welcome to CIIL")
st.header("Central Institute of Indian Languages")
st.subheader("Ministry of Education, Government of India")
st.markdown("Central Institute of Indian Languages was established to co-ordinate the development of Indian Languages, to bring about the essential unity of Indian ")
name = st.text_input("Enter your name :")
cname = st.text_input("Enter your course name :")
lname = st.text_input("Enter your language :")
adr = st.text_area("Enter your text : ")
classdate = st.selectbox("Enter your class : ",(1,2,3,4,5,6))

button = st.button("Submit")
if button :
    st.markdown(f"""
    name : {name}
    cname : {cname}
    lname : {lname}
    class : {classdate}""")
























