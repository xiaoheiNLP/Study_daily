# -*- coding:utf-8 -*-
"""
@author: xinquan
@file: class_super.py
@time: 2021/5/10 11:22 下午
@desc: 
"""
import sys
import os
import warnings
import datetime
warnings.filterwarnings('ignore')  # 忽略一些警告,可以删除
root_path = os.path.split(os.path.realpath(__file__))[0]  # 获取该脚本的地址,有效避免Linux和Windows文件路径格式不一致等问题,可以删除
print()

# 重写log_print方法，加入时间信息
def log_print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    print("当前时间：" + datetime.datetime.utcnow().now().strftime('%Y-%m-%d %H:%M:%S')) # 这样每次调用log_print()的时候，会先输出当前时间，然后再输出内容
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

if __name__ == '__main__':
    log_print()