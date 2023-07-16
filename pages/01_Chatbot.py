import streamlit as st

st.title("Create a chatbot")

def main():

    st.subheader("Upload Functionality")

    st.write("Choose a website URL or upload a file/directory to process.")
    website_url = st.text_input("Website URL")
    uploaded_file = st.file_uploader("Upload File/Directory")

    if st.button("Process"):
        crawled_pages = []
        uploaded_pages = []
           

main()