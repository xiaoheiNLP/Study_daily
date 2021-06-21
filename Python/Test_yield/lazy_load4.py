# -*-coding:utf-8-*-
# @Time    : 2019/10/30 0030 16:26
# @Author  :zhu
# @File    : lazy_load4.py
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
        standard_mode_diag = pd.read_excel(path + "/" + self.x, converters={"code": str})
        return standard_mode_diag


stand_icd10 = {
                "icd10_临床版2.0B": B(u"icd10_临床版2.0B（DRG用途代码）.xlsx"),
                "icd10_北京临床版v5.0": B(u"icd10_北京临床版v5.0.xlsx"),
                "icd10_北京临床版v6.0.xlsx": B(u"icd10_北京临床版v6.0.xlsx"),
                "icd10_医保版": B(u"icd10_医保版.xlsx"),
                "icd10_国家临床版2.0": B(u"icd10_国家临床版2.0_2.xlsx"),
                "icd10_国家临床版V1.1": B(u"icd10_国家临床版V1.1.xlsx"),
                "icd10_国家标准版": B(u"icd10_国家标准版.xlsx"),
                "icd10_广东标准版": B(u"icd10_广东标准版.xlsx")
            }


t1 = time.time()
print(len(stand_icd10))
print((stand_icd10["icd10_医保版"].getData()).head(5))
print("消耗时间是：",  time.time() - t1)
