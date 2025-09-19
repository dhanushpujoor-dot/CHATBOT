import speech_recognition as sr
import streamlit as st

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as source
with sr.Microphone() as source:
    print("🎤 Speak something...")
    audio = recognizer.listen(source,phrase_time_limit=5)

try:
    # Recognize speech using Google Web Speech API
    text = recognizer.recognize_google(audio)
    print("✅ You said:", text)
except sr.UnknownValueError:
    print("❌ Could not understand audio")
except sr.RequestError:
    print("⚠️ Could not request results (check your internet)")