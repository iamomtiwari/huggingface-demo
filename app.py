import gradio as gr
from transformers import pipeline

# Load the model
classifier = pipeline("sentiment-analysis")

# Define the function for Gradio
def analyze_sentiment(text):
    result = classifier(text)[0]
    return f"{result['label']} (Confidence: {result['score']:.2f})"

# Create a Gradio interface
interface = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text")

# Launch the app
interface.launch()
