# -*- coding:utf-8 -*-
"""
@author: xinquan
@file: task_regular.py
@time: 2021/4/22 9:46 上午
@desc: 
"""
import re
import os
import warnings

warnings.filterwarnings('ignore')  # 忽略一些警告,可以删除
root_path = os.path.split(os.path.realpath(__file__))[0]  # 获取该脚本的地址,有效避免Linux和Windows文件路径格式不一致等问题,可以删除


def task_1():
    pattern = re.compile(r'(；|\+|；|，|、|及)')
    result = re.split(pattern, 'a+b；c，d、e及f')
    print(result)


if __name__ == '__main__':
    task_1()
