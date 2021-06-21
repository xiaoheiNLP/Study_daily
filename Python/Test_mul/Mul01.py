# -*-coding:utf-8-*-
# @Time    : 2019/6/17 0017 16:24
# @Author   :zhuxinquan
# @File    : Mul01.py
"""
测试使用python 的多进程

"""
import pprint

def myprocess(mylist, i):
    mylist[i] += 10
    # return mylist
    return mylist



def test_orgin():
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(t)):
        myprocess(t, i)
    print(t)


def test_mul():
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    import multiprocessing
    from multiprocessing import Manager
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    t = Manager().list(t)
    for i in range(len(t)):
        pool.apply_async(myprocess, (t, i,))
    pool.close()
    pool.join()
    print(t)


if __name__ == '__main__':
    # test_orgin()
    test_mul()
    # t = "[1, 2, 4,5,67,8]"
    # t_1 = eval(t)
    # print(type(t_1))
    # print(t_1)