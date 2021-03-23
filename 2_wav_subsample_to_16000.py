import librosa
import soundfile as sf
import os
import re


base_dir = "./data/"
# base_dir = "./dict/"
subsample_dir = "./subsample_data/"
wav_pattern = re.compile(r'(.*)\.wav$')


li = os.listdir(base_dir)
for file_name in li:
    right_file_name = wav_pattern.match(file_name)
    if right_file_name is not None:
        src_sig, sr = sf.read(base_dir+file_name)  #name是要 输入的wav 返回 src_sig:音频数据  sr:原采样频率  
        dst_sig = librosa.resample(src_sig, sr, 16000)  #resample 入参三个 音频数据 原采样频率 和目标采样频率
        sf.write(base_dir+file_name, dst_sig, 16000)