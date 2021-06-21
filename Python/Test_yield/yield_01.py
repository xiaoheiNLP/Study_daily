# -*-coding:utf-8-*-
# @Time    : 2019/10/30 0030 14:46
# @Author  :zhu
# @File    : yield_01.py
# @task description :


def foo():
    print("starting...")
    t = 10
    while True:

        yield t
        t = t+1

g = foo()
print(g)
# print("*"*90)
print(next(g))
print("*"*20)
print(next(g))
print(next(g))
print(next(g))