# Image to Caption to Speech Conversion


This repository showcases a remarkable project that harnesses the capabilities of two Hugging Face Transformer models, converting images into text captions and then into speech. These functionalities are made accessible through a hosted API and a user-friendly web interface built with Streamlit.
Table of Contents

- Introduction
- Web Interface
- Requirements
- Contributing
![WebImg](1.png)
## Introduction

The "Image to Caption to Speech Conversion" project brings together cutting-edge technology to create a seamless conversion pipeline:

- Image to Text: We utilize a Hugging Face Transformer "Salesforce/blip-image-captioning-large" model specialized in converting images into descriptive text captions. This model employs advanced computer vision techniques to extract meaningful information from images.

- Text to Speech: Subsequently, we leverage another Hugging Face Transformer "espnet/kan-bayashi_ljspeech_vits" model API utilized, this time for converting text captions into lifelike speech. This component utilizes state-of-the-art text-to-speech synthesis capabilities.

The magic of this project doesn't stop there. We make these capabilities accessible through both an API and a web interface powered by Streamlit.

## Web Interface

The web interface, built with Streamlit, offers a user-friendly experience for image to caption and text to speech conversion. You can run the interface locally by following these steps:

### Clone the repository:

```bash
git clone https://github.com/ChiranthSH007/Image2Title2Speech_HuggingFaceTransformers_NLP
cd image-caption-speech-conversion
```
Install the required packages as listed in the Requirements section.

Run the Streamlit app:

```bash
streamlit run app.py
```
Access the app via the provided URL (usually, it's http://localhost:8501).

Upload an image, and the app will generate a text caption and play the corresponding speech.

## Requirements

To use and contribute to this project, ensure you have the following requirements installed:
```bash
    Python 3.x
    PyTorch
    Hugging Face Transformers
    Streamlit
    dotenv
```
You can install these packages using pip:

```bash
pip install torch transformers streamlit python-dotenv
```
## Contributing

Contributions to this project are encouraged. If you have suggestions or encounter issues, please create a GitHub issue. If you'd like to contribute code, fork the repository, make your changes in a feature branch, and submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
