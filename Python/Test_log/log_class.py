# -*-coding:utf-8-*-
# @Time    : 2019/8/26 0026 18:46
# @Author  : zhuxinquan
# @File    : log_class.py

import time

def timeit(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('消耗时间:', end - start)
    return wrapper

@timeit
def foo():
    print(u'祝鑫泉')


if __name__ == '__main__':
    foo()