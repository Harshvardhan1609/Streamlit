import streamlit as st

st.title("Hello Ji")
st.write("Radhe Radhe")
st.sidebar.write("Hello")
st.audio('net.mp3')
st.sidebar.image('hello.jpg')
a = "Harsh"
a = st.text_input("Enter your name")
st.sidebar.write(a)

b = st.sidebar.slider("Review your personality",min_value=0,max_value=100,value=20,step=1)

st.