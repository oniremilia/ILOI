import speech_recognition as sr
from pathlib import Path
import os 

# Ref: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
r = sr.Recognizer()

input_path = input("Enter the input file path: ")
with sr.AudioFile(input_path) as source:
    # listen for the data (load audio to memory)
    r.adjust_for_ambient_noise(source,duration=1)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    print("From file", input_path)
    try:
        text = r.recognize_google(audio_data, language="en-US") 
        print(text)
    except Exception as ex:
        print(ex)
            