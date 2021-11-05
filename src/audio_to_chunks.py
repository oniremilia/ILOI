from pydub import AudioSegment
from pathlib import Path
from pydub.utils import make_chunks

input_path = input("Enter the input file path: ")
output_path = input("Enter the output folder path: ")

find_name = input_path.rfind('/')
find_ex = input_path.rfind('.')
name = input_path[find_name+1:find_ex]

new_dir = output_path + "/" + name

Path(new_dir).mkdir(parents=True, exist_ok=True)

audio = AudioSegment.from_wav(input_path)
twenty_seconds = 20 * 1000
start_from_two_mins = audio[2*60*1000:]

chunks = make_chunks(start_from_two_mins, twenty_seconds)
for i, chunk in enumerate(chunks):
    temp_name = new_dir + '/' + name + "[" + str(i) + "]" + ".wav"
    chunk.export(temp_name, format="wav")