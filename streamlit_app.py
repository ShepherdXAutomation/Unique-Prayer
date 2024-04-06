import streamlit as st
from openai import OpenAI
import time
import os
import base64


st.set_page_config(page_title="Unique Prayer", page_icon="favicon.ico", layout="wide")
# Hide the top menu bar with the "hamburger" menu and Streamlit branding
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp { top: -50px; }
    </style>
    """, unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            .reportview-container .main footer {visibility: hidden;}
            /* Hide the running indicator */
            .reportview-container .main .status-indicator {display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

api_secret_key = os.environ.get("CHATGPT_API_KEY")



#api_key = st.secrets["CHATGPT_API_KEY"]
client = OpenAI(api_key=api_secret_key)
# Check if 'run_count' is already in the session state
# If it's not, initialize it to 0
if 'run_count' not in st.session_state:
    st.session_state['run_count'] = 0

st.session_state['run_count'] += 1

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
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_with_base64(src: str, width: str = "100px", alt: str = "Image"):
    """Generates an HTML img tag containing the image in base64 format with specified width"""
    base64_string = get_base64_of_bin_file(src)
    return f'<div style="text-align: center;"><img class="fade-in" src="data:image/png;base64,{base64_string}" alt="{alt}" style="width:{width};" />'


# Assuming your image is named 'your-image.png' and located in the same directory as your script
image_path = 'prayer_hands_transparent.png'

# Inject CSS animation and the image
st.markdown(custom_css, unsafe_allow_html=True)



# Display the fading text


welcome_placeholder = st.empty()

if st.session_state['run_count'] == 1:
    with welcome_placeholder.container():
        for i in range(3):
            if i == 0:
                st.markdown("<p class='fade-out'>hello</p>", unsafe_allow_html=True)
            if i == 1:
                st.markdown("<p class='fade-out'>would you like to...</p>", unsafe_allow_html=True)
            if i == 2:
                st.markdown("<p class='fade-out'>pray with me?</p>", unsafe_allow_html=True)
            time.sleep(3)

welcome_placeholder.empty()
with welcome_placeholder.container():
    st.markdown(get_img_with_base64(image_path, "80px"), unsafe_allow_html=True)
    st.markdown("<p class='fade-in'>The prayer app takes details you give it and generates a personal prayer for you. Everything you share here is completely private.</p>", unsafe_allow_html= True)
#st.markdown("<p class='fade-in'>The prayer app takes details you give it and generates a personal prayer for you. Everything you share here is completely private.</p>", unsafe_allow_html=True)
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
        {"role": "system", "content": "You are a christian pastor. The prayers you provide are in first person context (example: Dear lord, help and guide through my do. I pray for wisdom and peace). You provide prayers to users based off the details you give them. You also don't talk to the user except by giving them a prayer. You don't respond to questions."},
        {"role": "user", "content": request}
    ]
    )
    # Once the response is received, clear the loading message and display the response
    response_placeholder.empty()  # Clear the placeholder
    response_placeholder.write(completion.choices[0].message.content)  # Display the actual response

else:
    pass
