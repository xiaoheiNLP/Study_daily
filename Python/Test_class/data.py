# -*- coding:utf-8 -*-
"""
@author: xinquan
@file: data.py
@time: 2021/5/14 11:21 下午
@desc: 
"""

#
# class MyDict(object):
#     def __init__(self):
#         self.data = {}
#
#     def __len__(self):
#         return len(self.data)
#
#     def append(self, item):
#         self.data[len(self)] = item
#
#     def __getitem__(self, key):
#         if isinstance(key, int):
#             return self.data[key]
#         if isinstance(key, slice):
#             slicedkeys = list(self.data.keys())[key]
#             return {k: self.data[k] for k in slicedkeys}
#         else:
#             raise TypeError
#
# d = MyDict()
# d.append("My")
# d.append("name")
# d.append("is")
# d.append("Python猫")
# print(d)
# print(d[2])
# print(d[:2])
# print(d[-4:-2])
# print(d['hi'])

import pandas as pd
t_list = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
re_pd = pd.DataFrame(t_list)
print(re_pd)








