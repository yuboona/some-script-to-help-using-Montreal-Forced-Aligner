from pydub import AudioSegment
import os
import re
import shutil

base_dir = "./data/"
move_des_dir = "./data_mp3/"
lab_pattern = re.compile(r'(.*)\.lab$')


li = os.listdir(base_dir)
for file_name in li:
    right_file_name = lab_pattern.match(file_name)
    if right_file_name is not None:
        shutil.copy(base_dir+file_name, move_des_dir+file_name)
