# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 3:23 下午
# @Author  : xinquan
# @File    : profile_1.py


import line_profiler
import sys
# @profile
def fib(n):
    # 文件名aaa.py
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a+b
    return a
def bbb():
    for i in range(0, 3):
        print(i**2)
    print('end')


profile = line_profiler.LineProfiler(bbb)  # 把函数传递到性能分析器
profile.enable()  # 开始分析
bbb()
profile.disable()  # 停止分析
profile.print_stats(sys.stdout)  # 打印出性能分析结果

