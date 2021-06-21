# -*-coding:utf-8-*-
# @Time    : 2019/8/29 0029 18:00
# @Author  :zhu
# @File    : pandas_fasster_1.py
# @task description : 试试pandas加速
import pandas as pd
import time

def test_1():
    t1 = time.time()
    mydata = pd.read_excel('./(2019.08.13)----icd10_标准语料_v0.0.9.xlsx', sheet_name="Sheet1")
    t2 = time.time()
    print("加载消耗时间是：", t2 - t1)
    mydata[u'zhu'] = 0
    num_len = len(mydata)
    for row in range(0, num_len):
        print(row)
        mydata[u'zhu'].iloc[row] = mydata[u'zyzd_pre_bm'].str.len()
    t3 = time.time()
    print("遍历消耗时间是", t3 - t2)

    mydata.to_excel('xin.xlsx')
    t4 = time.time()
    print("存储消耗时间是", t4 - t3)


if __name__ == '__main__':
    test_1()




"""
https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653294130&idx=1&sn=42756891c73ab8b1ecbd6395efef4aba&chksm=802dcc27b75a4531d81719002ac6e62affe4c8e19b56347200bff0502ea44f6edddbbfdffdba&scene=7&key=d6b1e03f8b999503b7f41b712897798ae681c7a8247e484fccf6723d8a28f65ad4c548b3f41670ce7a21035c3c52720880c8620057235d64aec8a847cb5f6ac76d8bd657754baf7182ff359a94a3f220&ascene=0&uin=MTU0MjE4MzQ2Mw%3D%3D&devicetype=Windows+10&version=62060844&lang=zh_CN&pass_ticket=zILenfl61mntP%2FN6IXMHteXmCCydmMCGGia3ncHl55MehntQhOm7XEfRqz945wCU
"""
