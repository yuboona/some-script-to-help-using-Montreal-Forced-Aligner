# some-script-to-help-using-Montreal-Forced-Aligner

Some script for helping using [Montreal Forced Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/), 

- mainly for transforming Hanzi character to pinyin,
- generating phone dict,
- train your own model
- and extrat pause time from .textgrid files.

***In this project, I use [Common Voice](https://commonvoice.mozilla.org/zh-CN/datasets) Chinese dataset as example.*** *After extrating dataset.zip, please move clips directory to the path contains `common-voice-dataset-hanzi2pinyin.py` file. Then rename `clips` to `data`. Also make sure that `zh-CN` in that path.*

## Before traing with MFA(Montreal-Forced-Aligner)

1. `0_common-voice-dataset-hanzi2pinyin.py`, will generate `.lab` files in `data` dir.
2. `1_trans_mp3_to_wav_and_move_mp3_to_another.py`. Because Montreal-Forced-Aligner does not fit `.mp3` for training, I transformed it to `.wav` and moved `.mp3` to `data_mp3`.
3. Option. `1_copy_lab_to_data_mp3.py`
4. `2_wav_subsample_to_16000.py`, original `.wav` has many differnt speaker ratio. Using this scrip to change ratio.
5. `3_use_mfa_make_dict.sh`, generate a dictionary of pinyin phone. Make sure you set the right path parameter in `.sh`.

## Doing a training

`4_use_mfa_train_align_model.sh`, Training. Make sure you set the right path parameter in `.sh`.

## After traing, to produce pause time

1. `5_1_process_textgrid_mid_as_sp.py`, use `sp` and `sil` generated by MFA to extract pause time.
2. Or, `5_2_process_textgrid_only_sp.py`, use the middle timepoint of the every character to compute a difference time of two neighbor character.
