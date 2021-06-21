# -*- coding:utf-8 -*-
"""
@author: xinquan
@file: mytorch.py
@time: 2021/6/3 10:17 下午
@desc: 
"""
import os
import warnings

warnings.filterwarnings('ignore')  # 忽略一些警告,可以删除
root_path = os.path.split(os.path.realpath(__file__))[0]  # 获取该脚本的地址,有效避免Linux和Windows文件路径格式不一致等问题,可以删除


import torch
print("hellow pytorch {}".format(torch.__version__))
flag = True
if flag:
    t = torch.randint(0,9, size=(3,3))
    mask = t.ge(5)
    t_select = torch.masked_select(t, mask)
    print("t:\n{}\nmask:\n{}\nt_select:\n{}".format(t, mask, t_select))