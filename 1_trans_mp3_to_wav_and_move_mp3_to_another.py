from pydub import AudioSegment
import os
import re
import shutil

base_dir = "./data/"
move_des_dir = "./data_mp3/"
mp3_pattern = re.compile(r'(.*)\.mp3$')


li = os.listdir(base_dir)
for file_name in li:
    right_file_name = mp3_pattern.match(file_name)
    if right_file_name is not None:
        sound = AudioSegment.from_mp3(base_dir+file_name)
        sound.export(base_dir+right_file_name.group(1)+".wav", format='wav')
        shutil.move(base_dir+file_name, move_des_dir+file_name)
