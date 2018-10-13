# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:52:12 2018
@title: 天池大数据竞赛-分割训练集
@author: ff7f
@竞赛数据自行下载：https://tianchi.aliyun.com/competition/information.htm?spm=5176.100067.5678.2.133271eevUZ0SE&raceId=231688
"""
from glob import glob

files = glob('*.txt')
testfile = 'oppo_round1_test_A_20180929.txt'   # 测试集 16M 5万条未标注数据
validfile = 'oppo_round1_vali_20180929.txt'    # 验证集 16M 5万条标注数据
trainfile = 'oppo_round1_train_20180929.txt'   # 训练集 640M 2百万条标注数据

with open(testfile, encoding='utf8') as ftest, \
     open(validfile, encoding='utf8') as fvalid, \
     open(trainfile, encoding='utf8') as ftrain:
    
    # 读入测试集
    testset = ftest.readlines()
    print(f'>>> 读入测试集[{testfile}]\n测试集记录数：{len(testset)}，记录长度：{len(testset[100])}')
    
    # 读入验证集
    validset = fvalid.readlines()
    print(f'>>> 读入验证集[{validfile}]\n验证集记录数：{len(validset)}，记录长度：{len(validset[100])}')
    
    # 读入训练集
    trainset = data = ftrain.read().split('\n')
    print(f'>>> 读入训练集[{trainfile}]\n训练集记录数：{len(trainset)}，记录长度：{len(trainset[100])}')
    
# 分割trainfile,5万条1个文件，2百万条共40个文件
batch = 50000
filename = 'train%s.txt'
path = 'trainset\\' + filename
print('>>> 开始分割训练集。。')
for n in range(40):
    print((filename % (n+1)).ljust(13), end='')
    fileblock = '\n'.join(trainset[n*batch: (n+1)*batch])
    with open(path % (n+1), 'w', encoding='utf8') as f:
        f.write(fileblock)
    if (n+1) % 5 == 0:
        print('')
print('\n>>> 训练集分割完成，共分40个文件。。')
    