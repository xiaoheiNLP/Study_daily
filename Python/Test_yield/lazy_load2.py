# -*-coding:utf-8-*-
# @Time    : 2019/10/30 0030 15:27
# @Author  :zhu
# @File    : lazy_load2.py
# @task description :
import lazy_object_proxy as lazy_zhu
import pandas as pd
import pysnooper
path = r"C:\Users\Administrator\Desktop\myframe2\\tffscode-master\\table"

# standard_mode_diag = pd.read_excel(path+u"/icd10_临床版2.0B（DRG用途代码）.xlsx", converters={"code": str})


# @pysnooper.snoop()
def test1():
    def expensive_func(t):
        # standard_mode_diag = pd.read_excel(path+u"/icd10_临床版2.0B（DRG用途代码）.xlsx", converters={"code": str})
        print("kakkakakakakaklalallaalla")
        return t

    obj = lazy_zhu.Proxy(expensive_func)
    print("go....")
    print(obj)
    # stand_icd10 = {
    #     "icd10_临床版2.0B（DRG用途代码）": lazy_zhu.Proxy(expensive_func),
    #                }
    # print("1")
    # print(len(stand_icd10))  # now expensive_func is called
    # print("2")
    # print(len(stand_icd10))   # the result without calling the expensive_func
    # print(stand_icd10["icd10_临床版2.0B（DRG用途代码）"][])


if __name__ == '__main__':
    test1()


