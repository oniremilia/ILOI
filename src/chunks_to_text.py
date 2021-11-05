import speech_recognition as sr
from pathlib import Path
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
#from scipy.io import wavfile
#import noisereduce as nr

# Ref: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python

input_path = input("Enter the input file path: ")

# load data
#rate, data = wavfile.read(input_path)
# perform noise reduction
#reduced_noise = nr.reduce_noise(y=data, sr=rate)

r = sr.Recognizer()

with sr.AudioFile(input_path) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
'''
audio = AudioSegment.from_wav(input_path)  
# split audio sound where silence is 700 miliseconds or more and get chunks
chunks = split_on_silence(audio,
    # experiment with this value for your target audio file
    min_silence_len = 200,
    # adjust this per requirement
    silence_thresh = audio.dBFS-14,
    # keep the silence for 1 second, adjustable as well
    keep_silence= 1000,
)
folder_name = "audio-chunks"
# create a directory to store the audio chunks
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
whole_text = ""
# process each chunk 
for i, audio_chunk in enumerate(chunks, start=1):
    # export audio chunk and save it in
    # the `folder_name` directory.
    chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
    audio_chunk.export(chunk_filename, format="wav")
    # recognize the chunk
    with sr.AudioFile(chunk_filename) as source:
        audio_listened = r.record(source)
        # try converting it to text
        try:
            text = r.recognize_google(audio_listened)
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text
print(whole_text)
'''