from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
import os
import streamlit as st

# create .env file and add HUGGINGFACE_API_TOKEN
load_dotenv(find_dotenv())  # load the .env file
# hugging face User Access Tokens
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Image to Text Conversion using "Salesforce/blip-image-captioning-large" model from Hugging Face


def img2txt(url):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-large")
    text = image_to_text(url)

    print(text)
    return text

# Text to Speech Conversion using "espnet/kan-bayashi_ljspeech_vits"  implemented using API of Huggingface


def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

    payload = {
        "inputs": message
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    print(response)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)

# StreamLit to create web page


def main():
    st.set_page_config(page_title="Image 2 Audio", page_icon="-")

    st.header("Turn Image into Audio")
    uploaded_file = st.file_uploader("Choose an image ...", type="jpg")

    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption="Uploaded Image",
                 use_column_width=True)
        message = img2txt(uploaded_file.name)
        text2speech(message[0]["generated_text"])

        with st.expander("Image Caption"):
            st.write(message[0]["generated_text"])

        st.audio("audio.flac")


if __name__ == '__main__':
    main()
