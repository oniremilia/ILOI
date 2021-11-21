import moviepy.editor as mp
from pathlib import Path
from pydub import AudioSegment
from pathlib import Path
from pydub.utils import make_chunks
import os
import pandas as pd
def vedio2audio(input_path):
    output_path = './audio'
    Path(output_path).mkdir(parents=True, exist_ok=True)

    find_name = input_path.rfind('/')
    find_ex = input_path.rfind('.')
    name = input_path[find_name + 1:find_ex]

    # Insert Local Video File Path
    clip = mp.VideoFileClip(input_path)

    # Insert Local Audio File Path
    clip.audio.write_audiofile(output_path + '/' + name + ".wav")

def audio2chunks(input_path, vedio_time):
    output_path = './chunks'

    find_name = input_path.rfind('/')
    find_ex = input_path.rfind('.')
    name = input_path[find_name + 1:find_ex]

    new_dir = output_path + "/" + name

    Path(new_dir).mkdir(parents=True, exist_ok=True)

    audio = AudioSegment.from_wav(input_path)
    twenty_seconds = 20 * 1000
    # start_from_two_mins = audio[2 * 60 * 1000:]
    start_from = audio[vedio_time[name] * 60 * 1000:]

    chunks = make_chunks(start_from, twenty_seconds)
    for i, chunk in enumerate(chunks):
        # temp_name = new_dir + '/' + name + "[" + str(i) + "]" + ".wav"
        temp_name = new_dir + '/' + "chunks" + "_" + str(i) + ".wav"
        chunk.export(temp_name, format="wav")

if __name__ == '__main__':
    data = pd.read_csv('./time_sheet.csv')
    vedio_time = {}
    for index, row in data.iterrows():
        h, m, s = row['time'].strip().split(':')
        vedio_time[row['name']] = int(m)
    # print(vedio_time)
    all_file_list = []
    for root, dirs, files in os.walk("./vedio", topdown=False):
        for name in files:
            all_file_list.append(os.path.join(root, name))
    print(all_file_list)

    for input_path in all_file_list:
        vedio2audio(input_path)
        find_name = input_path.rfind('/')
        find_ex = input_path.rfind('.')
        name = input_path[find_name + 1:find_ex]
        audio2chunks('./audio/'+name+'.wav', vedio_time)