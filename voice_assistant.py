import streamlit as st

st.set_page_config(
    page_title = "Voice Assistant",
    layout = "wide"
)

# Libraries
import os
import time
import pyttsx3
import speech_recognition as sr   # speech to text
from groq import Groq
from dotenv import load_dotenv

# loading the API Key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# initialize the LLM model
client = Groq(api_key = GROQ_API_KEY)
MODEL = "llama-3.3-70b-versatile"

# initialize the speech to text recognizer
@st.cache_resource
def get_recognizer():
    return sr.Recognizer()

recognizer = get_recognizer()

# initialize Text to Speech engine
def get_tts_engine():
    try:
        engine = pyttsx3.init()
        return engine
    except Exception as e:
        print(f"Failed to initialize TTS Engine: {e}")
        return None

def main():
    st.title("Baby Siri Voice Assistant")


if __name__ == "__main__":
    main()