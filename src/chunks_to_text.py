import speech_recognition as sr
from pathlib import Path
import os 

# Ref: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
r = sr.Recognizer()

input_path = input("Enter the input file path: ")
for file in os.listdir(input_path):
    filename = os.fsdecode(file)
    if filename.endswith(".wav"): 
        file_p = os.path.join(input_path, filename)
        with sr.AudioFile(file_p) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            print("From file", file_p)
            try:
                text = r.recognize_google(audio_data) 
                print(text)
            except:
                print("Error: Nothing detected in this file")
            