# 手册

1. conda create -n aligner -c conda-forge openblas python=3.8 openfst pynini ngram baumwelch
2. conda activate aligner
3. pip install montreal-forced-aligner
4. mfa thirdparty download 安装不上,直接复制网站下载,放入到路径
5. 下载g2p模型,网不好直接用网址
6. 使用g2p生成字典,会出问题,要改pynini版本为2.1.0
7. 训练对齐模型,会缺少openblas,把路径export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/anaconda3/envs/aligner/lib/
8. 开始训练

会有beam too narrow的问题, doubling the beam width in aligner/config/basic_align.yaml. basic_train.yaml 把beam参数加倍

1. basic_train.yaml
2. mfa模块的入口文件是 /home/zz/anaconda3/envs/aligner/lib/python3.8/site-packages/montreal_forced_aligner/command_line/mfa.py
3. mfa.py-->train_and_align.py-->train_config.py 的 load_basic_train()