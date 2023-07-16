import streamlit as st
import requests
import json
import os



def main():
    st.set_page_config(
        page_title="AI App"
    )
    st.title("AI App using OpenAI ")

    # Left section with collapsible menu navigation
    st.subheader("please enter your openai api key to run this application")
    OPENAI_API_KEY = st.text_input("OpenAi API Key")
    
main()