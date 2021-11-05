import moviepy.editor as mp
from pathlib import Path

input_path = input("Enter the input file path: ")
output_path = input("Enter the output folder path: ")
Path(output_path).mkdir(parents=True, exist_ok=True)

find_name = input_path.rfind('/')
find_ex = input_path.rfind('.')
name = input_path[find_name+1:find_ex]

# Insert Local Video File Path 
clip = mp.VideoFileClip(input_path)
  
# Insert Local Audio File Path
clip.audio.write_audiofile(output_path + '/' + name + ".wav")