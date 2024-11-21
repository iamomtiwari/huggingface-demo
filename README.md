Access from: https://huggingface.co/spaces/iamomtiwari/Sentiment_demo
# Hugging Face Sentiment Analysis App

This project is a sentiment analysis app built with Hugging Face Transformers and Gradio.

## Features
- Sentiment analysis using the `distilbert-base-uncased-finetuned-sst-2-english` model.
- Simple web interface powered by Gradio.

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/iamomtiwari/huggingface-demo.git
   cd huggingface-demo
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py
