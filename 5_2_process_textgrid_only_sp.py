import os
import sys
import numpy as np

from pypinyin import pinyin, lazy_pinyin, Style
import re
import textgrid

base_dir = "./"
# root_dir = "./train/"
root_dir = "./my_aligned_textgrid/"
pause_time_dir = "./out_textgrid_only_sp/"
pattern = re.compile(r'(.*)\.TextGrid$')


for root, dir, files in os.walk(root_dir):
    for filename in files:
        out_file_ptn = pattern.match(filename)
        if out_file_ptn is not None:
            tg = textgrid.TextGrid()
            tg.read(root_dir+filename)  # 'file.TextGrid' 是文件名
            pause_time_start = 0.0
            count = 0
            current_character = "start"
            out_file = pause_time_dir + out_file_ptn.group(1) + ".sp"
            # 处理每一个文件
            with open(out_file, mode="w") as out:
                for index, i in enumerate(tg.tiers[0]):
                    if i.mark != "":
                        # print("asdasd", i.mark)
                        # 当前字的pause_time
                        pause_time = i.minTime - pause_time_start
                        print(current_character, "pause_time:", pause_time)
                        if current_character != "start":
                            out.write("{}".format(pause_time))
                            out.write("\n")
                        # 更新当前字
                        current_character = i.mark
                        pause_time_start = i.maxTime
                        count += 1
