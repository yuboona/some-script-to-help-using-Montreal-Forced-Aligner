# coding:utf8
import os
import sys
import numpy as np
from pypinyin import pinyin, lazy_pinyin, Style
import re
import csv
from zhon.hanzi import punctuation

base_dir = "./"
# root_dir = "./train/"
root_dir = "./zh-CN/"
mp3_dir = "./data/"
# pattern = re.compile(r'(.*)\.mp3$')
mp3_pattern = re.compile(r'(.*)\.mp3$')
tsv_pattern = re.compile(r'.*\.tsv$')


def solve_csv(csv_path, write_pinyin_dir):
    print(csv_path)
    with open(csv_path) as in_file:
        csv_content = csv.reader(in_file, delimiter='\t')
        print(csv_content)
        # row[1]是path row[2]是sentence
        for csv_line in csv_content:
            # print(csv_line)
            if csv_line[1] == "path":
                print(csv_line)
            else:
                # 需要将str转换为unicode
                write_lab_file_name = mp3_pattern.match(csv_line[1]).group(1) + ".lab"
                write_pinyin_file_path = write_pinyin_dir + write_lab_file_name
                # 去除标点
                csv_line_without_punc = re.sub("[%s]+" % punctuation, "", csv_line[2])
                # 汉字转拼音
                pinyin_str = lazy_pinyin(csv_line_without_punc,
                                         style=Style.TONE3,
                                         neutral_tone_with_five=True)
                pinyinline = ' '.join(pinyin_str)
                with open(write_pinyin_file_path, "w") as w:
                    w.write(pinyinline)


li = os.listdir(root_dir)
for file_name in li:
    right_file_name = tsv_pattern.match(file_name)
    if right_file_name is not None:
        print(file_name)
        write_pinyin_dir = mp3_dir
        solve_csv(root_dir + file_name, write_pinyin_dir)
