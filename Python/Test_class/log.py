# -*- coding:utf-8 -*-
"""
@author: xinquan
@file: log.py
@time: 2021/5/12 5:05 下午
@desc: 打印函数运行时间和打印到文件
"""
import os
import sys
import warnings

warnings.filterwarnings('ignore')  # 忽略一些警告,可以删除
root_path = os.path.split(os.path.realpath(__file__))[0]  # 获取该脚本的地址,有效避免Linux和Windows文件路径格式不一致等问题,可以删除
import time
import functools


def print_to_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log_file = open("message.log", "a+")
        sys.stdout = log_file
        res = func(*args, **kwargs)
        log_file.close()
        return res

    return wrapper


def log_zhu(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'函数 {func.__name__} 耗时 {(end - start) * 1000} ms')
        return res

    return wrapper


@print_to_log
def cal_time(a):
    a = [1, 2, 4, 5, 6, a]
    d = sum(a)
    print(d)


if __name__ == '__main__':
    cal_time(510)
