import streamlit as st
import time
# Custom CSS for fading effect
custom_css = """
<style>
    .fade-out {
        animation: fadeOut 3s ease-in-out forwards;
    }

    @keyframes fadeOut {
        0% {
            opacity: 1;
        }
        100% {
            opacity: 0;
        }
    }
    .fade-in {
     animation: fadeIn 1s ease-in-out forwards;
    }
    @keyframes fadeIn {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
</style>
"""
placeholder = st.empty()
# Display the fading text
st.markdown(custom_css, unsafe_allow_html=True)


for i in range(3):
    if i == 0:
        st.markdown("<p class='fade-out'>hello.</p>", unsafe_allow_html=True)
    if i == 1:
        st.markdown("<p class='fade-out'>would you like to...</p>", unsafe_allow_html=True)
    if i == 2:
       st.markdown("<p class='fade-out'>pray with me?</p>", unsafe_allow_html=True)
    time.sleep(3)

st.empty()
st.markdown("<p class='fade-in'>The prayer app takes details you give it and generates a personal prayer for you. Everything you share here is completely private.</p>", unsafe_allow_html=True)
st.text_input("Tell me your troubles, my child.")
