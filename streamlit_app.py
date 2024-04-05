import streamlit as st
import time
from openai import OpenAI

api_key = st.secrets["CHATGPT_API_KEY"]
client = OpenAI(api_key)

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


st.markdown("<p class='fade-in'>The prayer app takes details you give it and generates a personal prayer for you. Everything you share here is completely private.</p>", unsafe_allow_html=True)

request = st.text_input("Tell me your troubles, my child.", key="request")
response_placeholder = st.empty()
# Conditional check to see if the user has entered some text and pressed Enter.
if request:
  # Display a loading message in the placeholder
    with response_placeholder.container():
        st.write("Generating your personal prayer, please wait...")

    # Simulate the delay or function to get ChatGPT response here
    # This is where you'd make the API call to ChatGPT and wait for the response
    # For demonstration, I'm replacing it with a simulated response after a delay
    # time.sleep(2)  # Simulating response time, remove when using real API call
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a christian pastor. The prayers you provide are in first person context (example: Dear lord, help and guide through my do. I pray for wisdom and peace). You provide prayers to users based off the details you give them."},
        {"role": "user", "content": request}
    ]
    )
    # Once the response is received, clear the loading message and display the response
    response_placeholder.empty()  # Clear the placeholder
    response_placeholder.write(completion.choices[0].message.content)  # Display the actual response

else:
    pass
