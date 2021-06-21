# -*-coding:utf-8-*-


"""
测试所有的排序

"""

import sys
sys.setrecursionlimit(10000)


from a_Bubble_sort import bubbleSort
from b_Select_Sort import selectSort
from c_Insert_Sort import insertSort
from d_Quick_Sort import quickSort
from e_Heap_Sort import heapSort
from f_Merge_Sort import mergeSort
from g_Radix_Sort import radixSort
from h_Count_Sort import countSort
from i_Shell_Sort import shellSort
from j_BucketSort import bucketSort

import numpy as np
import pickle
import time


# 数据的格式化存储
class Data_in_out():
    def load_data(self, myaddress):
        t_1 = time.time()
        fopen = open(myaddress, 'rb')
        print('读取数据消耗时间：', time.time() - t_1)
        return pickle.load(fopen)

    def dump_data(self, mydata, myaddress):
        fopen = open(myaddress, 'wb')
        pickle.dump(mydata, fopen)
        fopen.close()


"""先定义几个数据：1.百级的数组  2，千级数组  3.万级数组  4.十万级数组"""
def create_data():

    t_100 = np.random.permutation(100)
    t = np.random.seed(0)
    print(t_100)
    print(len(t_100))

    t_1000 = np.random.permutation(1000)
    print(t_1000)
    print(len(t_1000))

    t_10000 = np.random.permutation(10000)
    print(len(t_10000))

    t_100000 = np.random.permutation(100000)
    print(len(t_100000))

    t_1000000 = np.random.permutation(1000000)
    print(len(t_1000000))

    data_in_out = Data_in_out()
    data_in_out.dump_data(t_100, './test_data/t_100.pkl')
    data_in_out.dump_data(t_1000, './test_data/t_1000.pkl')
    data_in_out.dump_data(t_10000, './test_data/t_10000.pkl')
    data_in_out.dump_data(t_100000, './test_data/t_100000.pkl')
    data_in_out.dump_data(t_1000000, './test_data/t_1000000.pkl')


def test_sort(t_100, t_1000, t_10000, t_100000, t_1000000):

    t_1 = time.time()
    quickSort(t_100)
    print("百级排序消耗时间：", time.time() - t_1)

    t_1 = time.time()
    quickSort(t_1000)
    print("千级排序消耗时间：", time.time() - t_1)

    t_1 = time.time()
    quickSort(t_10000)
    print("万级排序消耗时间：", time.time() - t_1)
    #
    t_1 = time.time()
    quickSort(t_100000)
    print("十万级排序消耗时间：", time.time() - t_1)

    t_1 = time.time()
    quickSort(t_1000000)
    print("十万级排序消耗时间：", time.time() - t_1)


if __name__ == '__main__':
    # create_data()
    # exit()
    # data_in_out = Data_in_out()
    # t_100 = data_in_out.load_data('./test_data/t_100.pkl')
    # t_1000 = data_in_out.load_data('./test_data/t_1000.pkl')
    # t_10000 = data_in_out.load_data('./test_data/t_10000.pkl')
    # t_100000 = data_in_out.load_data('./test_data/t_100000.pkl')
    # t_1000000 = data_in_out.load_data('./test_data/t_1000000.pkl')
    # print("*"*89)
    # test_sort(t_100, t_1000, t_10000, t_100000, t_1000000)

    t_list = [1, 4, 6, 5, 2, 8, 7, 9]

    for i in range(10):
        t_list.extend(t_list)

    import time
    print("lllll")
    t1 = time.time()
    quickSort(t_list)
    print('a')
    t2 = time.time()
    bucketSort(t_list)
    t3 = time.time()

    print(t2 - t1)
    print(t3 - t2)

"""
十万级排序消耗时间： 1.7750649452209473
十万级排序消耗时间： 28.019365072250366

十万级排序消耗时间： 1.0693469047546387
十万级排序消耗时间： 12.150224924087524

"""