# -*-coding:utf-8-*-
# @Time    : 2019/11/15 0015 15:11
# @Author  :zhu
# @File    : Example_1.py
# @task description :
import pandas as pd
import numpy as np


def jugeContain(x, y, num):
    """
    :param x: 字符串
    :param y: 字符串
    :param num: int
    :return: int
    """
    if isinstance(x, (float, int)):
        x = str(x)
    if isinstance(y, (float, int)):
        y = str(y)
    try:
        if x in y:
            return num
        else:
            return 0
    except:
        return 0


def recommendLocal(data):   # 推荐编码的
    """
    :param data: DataFrame类型，其中数据为icd10/icd9 的推荐结果
    :return: DataFrame类型，返回的数据是在输入的基础上，按照icd10/9 从10个推荐结果中提取第一次匹配到 前5为或者前3位 的推荐结果，并将其作为最后的推荐结果。
    """
    flag = np.logical_not(np.zeros(data.shape[0], dtype=np.bool))   # 逻辑非:取反的意思
    print(flag)
    for num in [5, 4]:
        for i in range(10):
            if num == 5:
                try:
                    t = list(map(
                        lambda x, y: jugeContain(x, y, 5), data.loc[flag, 'jbdm'].str[:num],
                        data.loc[flag, 'predict%s' % i]))
                    data.loc[flag, 'mark'] = t
                except:
                    print(u"mark阶段出现错误1")
                    continue
            else:
                try:
                    data.loc[flag, 'mark'] = list(map(lambda x, y: jugeContain(x, y, 4), data.loc[flag, 'jbdm'].str[:num], data.loc[flag, 'predict%s' % i]))
                except:
                    print(u"mark阶段出现错误2")
                    continue
            data.loc[flag, "recommend"] = data.loc[flag, 'predict%s' % i]
            flag1 = data['mark'] == 0
            flag = flag & flag1
    return data



if __name__ == '__main__':
    data = pd.read_excel("./zhu1.xlsx")
    result_data = recommendLocal(data)
    # print(result_data.head(5))