# -*-coding:utf-8-*-
# @Time    : 2019/12/17 0017 10:42
# @Author  :zhu
# @File    : sample_02.py
# @task description :
"""
将numpy的数据直接转换成pd.DataFrame
"""
import numpy as np
import pandas as pd


if __name__ == '__main__':
    t = np.zeros((5, 9))
    print(t)
    exit()
    t[1][1] = 9999
    mypd = pd.DataFrame(t)
    print(t)
    print()
    print(mypd)
    mypd.to_excel("./zhu.xlsx")
