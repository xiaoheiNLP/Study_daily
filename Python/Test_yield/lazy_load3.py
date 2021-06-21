# -*-coding:utf-8-*-
# @Time    : 2019/10/30 0030 16:04
# @Author  :zhu
# @File    : lazy_load3.py
# @task description :

import pandas as pd
import time
from lazy_object_proxy import Proxy
path = r"C:\Users\Administrator\Desktop\myframe2\\tffscode-master\\table"

def lazy(cls):
    class Lazy:
        def __new__(cls, *args, **kwargs):
            original_class = type(object.__name__, (cls,), {})
            original_class.__new__ = lambda cls_, *args_, **kwargs_: object.__new__(cls_)
            return Proxy(lambda: original_class(*args, **kwargs))
    lazy_class = type(cls.__name__, (cls, Lazy), {})
    return lazy_class


@lazy
class B:
    def __init__(self, x):
        self.x = x

    def getData(self):
        print("实现了")
        standard_mode_diag = pd.read_excel(path + "/" + self.x, converters={"code": str})
        return standard_mode_diag

# b = B(u"icd10_临床版2.0B（DRG用途代码）.xlsx")
stand_icd10 = {
            "icd10_临床版2.0B":B(u"icd10_临床版2.0B（DRG用途代码）.xlsx"),

            }
t1 = time.time()
print(len(stand_icd10))
print("消耗时间是：",  time.time() - t1)
