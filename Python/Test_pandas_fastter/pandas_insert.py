# -*-coding:utf-8-*-
# @Time    : 2019/10/29 0029 12:45
# @Author  :zhu
# @File    : pandas_insert.py
# @task description :

import pandas as pd
data = {'BoolCol': [1, 2, 3, 3, 4],
        'attr': [22, 33, 22, 44, 66],
        'BoolC': [1, 2, 3, 3, 4],
        'att': [22, 33, 22, 44, 66],
        'Bool': [1, 2, 3, 3, 4]
        }
df = pd.DataFrame(data, index=[10, 20, 30, 40, 50])
print(df)
print('.'.join(
    map(lambda x: str(x), [1, 2, 4, 5])
))