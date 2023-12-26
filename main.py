from dotenv import load_dotenv  
import os
import streamlit as st
from openai import OpenAI


def init():
    load_dotenv()  # Load environment variables from a .env file.

    # Load the OpenAI API key from an environment variable.
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPEN_API_KEY") == "":
        print(">> OPENAI_API_KEY is not set")
        exit(1)
    else: 
        print(">> OPENAI_API_KEY is set")
    
    # Define Streamlit page configuration.
    st.set_page_config(
        page_title="Image Creating Bot using DALL.E",   # Title of the page.
        page_icon="👨🏼‍🎨"                                  # Icon of the page.
    )
    
    
# Clearing input field
def clear_text():
    global input_value 
    input_value = st.session_state.user_input
    st.session_state.user_input = ""


# Main
def main():
    init() # initialization
    
    # Header of the page
    st.header("Image Creating Bot using DALL.E 👨🏼‍🎨")
    
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    
    st.text_input("Image prompt: ", on_change=clear_text(), key="user_input")
    
    client = OpenAI()
    
    if input_value:
        response = client.images.generate(
            model="dall-e-3",
            prompt=input_value,
            size="1024x1024",               
            quality="standard",              # options: "hd" or "standard"
            n=1,                             # create 1 image
        )
        st.caption(input_value)
        response.data[0].url


if __name__ == '__main__':
    main()