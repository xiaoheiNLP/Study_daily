# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 9:50 下午
# @Author  : xinquan
# @File    : pandas_Everything.py
"""
首先,pandas的官方API文档地址是:
    https://pandas.pydata.org/pandas-docs/stable/reference/index.html

记录一些自己经常忘记又常用的知识点；
也记录一下新知识点的测试，尤其是加速的知识点；

pandas的基本使用
1.pandas的初始化
2.pandas的遍历
3.pandas的透视表
4.pandas的加速

"""
import pandas as pd
import numpy as np


def yfunc1_pandas():
    """_
    DataFrame的初始化
    :return:
    """
    # 1.通过list
    df1 = pd.DataFrame([['a1', 1]], columns=["uid", "score"])
    print(df1)
    print()
    # 2.通过dict
    df2 = pd.DataFrame({'col1': np.arange(3), 'col2': np.arange(5, 8)})
    print(df2)
    """
    获取表名：table_name_list = pd.ExcelFile(upath2)
    获取列名：print(data.columns.values)
    """

def func2_pandas():
    """
    pandas的各种遍历
    函数有
        loc  :列取值函数,根据index来索引对应的行
        iloc :列取值函数,并不是根据index来索引，而是根据行号来索引，行号从0开始，逐次加1。
        所以以上2个函数经常用来做筛选

        apply  :号称pandas函数中自由度最高的函数, 和groupby结合使用能虐出新天地,但apply一直被吐槽比较慢
        agg

        map :
        applymap :遍历pandas所有的元素
    :return:
    """
    # 1.loc和iloc
    # df1 = pd.DataFrame([['a1', 1], ['a2', 4], ['a1', 1], ['a2', 4]], columns=["uid", "score"])
    # print(df1)
    # print()
    # print(df1.loc[df1["score"]>1])
    # print()
    # # print(df1.iloc[1])
    # print(df1.loc[0:1])

    # 2.apply
    frame = pd.DataFrame({
        'key1': ['a', 'b', 'c', 'd'],
        'key2': ['one', 'two', 'three', 'four'],
        'data1': np.arange(4),
        'data2': np.arange(5, 9)
    })
    print(frame)
    print()
    frame['data1'] = frame['data1'].map(lambda x: x+5)
    print(frame)
    print()
    """重点比较一下这两个例子"""
    frame['total'] = frame[['data1', 'data2']].apply(lambda x: x.sum(), axis=1)
    # print(frame)
    # frame.loc['total'] = frame[['data1', 'data2']].apply(lambda x: x.sum(), axis=0)
    # print(frame)

    print(frame)


def func3_pandas():
    """
    pandas的透视表
    学习参考地址:
        https://www.cnblogs.com/Yanjy-OnlyOne/p/11195621.html
    透视表的官方地址:
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html
    """
    df = pd.read_csv('./James_Harden.csv', encoding='utf8')
    # df_1 = pd.pivot_table(df, index=[u'对手'])

    """
    当我们未设置aggfunc时，它默认aggfunc='mean'计算均值。
    我们还想要获得james harden在主客场和不同胜负情况下的总得分、总篮板、总助攻时：
    """
    df_1 = pd.pivot_table(df, index=[u'对手'], values=[u'得分', u'助攻', u'篮板'], aggfunc=[np.sum, np.max, np.mean])
    print()
    df_1.to_csv("./zhu1.csv")

    table = pd.pivot_table(df, index=[u'对手', u'胜负'], columns=[u'主客场'], values=[u'得分', u'助攻', u'篮板'],
                           aggfunc={u'得分': np.mean, u'助攻': [min, max, np.mean]}, fill_value=0)
    
"""pandas加速的三个测试"""
def func4_pandas_1():
    """
    pandas的加速:
    1.第三方包:Swifter
    学习资料地址:https://mp.weixin.qq.com/s/wMnOu3qwLiZFm8yTN31cQA
    github地址:https://github.com/jmcarpenter2/swifter

    Swifter是一个“以最快的方式将任何函数应用于Pandas dataframe或series”的库。
    Swifter可以检查你的函数是否可以向量化，如果可以，就使用向量化计算

    2.加速策略:
    地址:https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653294130&idx=1&sn=42756891c73ab8b1ecbd6395efef4aba&chksm=802dcc27b75a4531d81719002ac6e62affe4c8e19b56347200bff0502ea44f6edddbbfdffdba&token=607437153&lang=zh_CN&scene=21#wechat_redirect
    :return:
    """
    import time
    import swifter

    df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [5, 6, 7, 8]})
    df1 = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [5, 6, 7, 8]})
    df2 = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [5, 6, 7, 8]})
    t1 = time.time()
    for i in range(10000):
        df1['x2'] = df1['x'].apply(lambda x: x ** 2)
    t2 = time.time()
    print("1消耗时间:", t2 - t1)
    print()
    def func_map(x):
        return x ** 2

    for i in range(10000):
        df2["x2"] = list(map(func_map, df2["x"]))
    t3 = time.time()
    print("2消耗时间:", t3 - t2)
    print()
    for i in range(10000):
        df['x2'] = df['x'].swifter.apply(lambda x: x ** 2)
    t4 = time.time()
    print("3消耗时间:", t4 - t3)


    """
    # runs on multiple cores
    df['x2'] = df['x'].swifter.apply(lambda x: x ** 2)

    # use swifter apply on whole dataframe
    df['agg'] = df.swifter.apply(lambda x: x.sum() - x.min())

    # use swifter apply on specific columns
    df['outCol'] = df[['inCol1', 'inCol2']].swifter.apply(my_func)
    df['outCol'] = df[['inCol1', 'inCol2', 'inCol3']].swifter.apply(my_func,
                                                                    positional_arg, keyword_arg=keyword_argval)

    """


def func4_pandas_2():
    """
    pandas的加速:
    2.加速策略:
    地址:https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653294130&idx=1&sn=42756891c73ab8b1ecbd6395efef4aba&chksm=802dcc27b75a4531d81719002ac6e62affe4c8e19b56347200bff0502ea44f6edddbbfdffdba&token=607437153&lang=zh_CN&scene=21#wechat_redirect
    :return:
    """
    df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [5, 6, 7, 8]})
    print(df)


def func4_pandas_3():
    """
    地址:https://stackoverflow.com/questions/52673285/performance-of-pandas-apply-vs-np-vectorize-to-create-new-column-from-existing-c

    https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653294130&idx=1&sn=42756891c73ab8b1ecbd6395efef4aba&chksm=802dcc27b75a4531d81719002ac6e62affe4c8e19b56347200bff0502ea44f6edddbbfdffdba&token=607437153&lang=zh_CN&scene=21#wechat_redirect
    :return:
    """
    import seaborn as sns
    import time
    data = sns.load_dataset("iris")
    print(data.head())

    """
    0.01345
    0.005892
    0.0020897秒
    """
def func4_pandas_4():
    df1 = pd.DataFrame([['a1', 1, 1], ['a2', 4, 4], ['a0', 6, 0]], columns=["uid", "score1", "score2"])
    print(df1)
    print()
    print(df1.max())
    print()
    print(df1.loc[:, "score1"].max())


"""
几个炫酷的操作:
1.做转换的时候
    level_map = {1: 'high', 2: 'medium', 3: 'low'}
    df['c_level'] = df['c'].map(level_map)

2.pandas的去重
myPD.drop_duplicates(subset=["nameKey", "codeKey"], keep='first', inplace=True)
"""



if __name__ == '__main__':
    func4_pandas_4()
    exit()
    print(id)
    exit()
    yfunc1_pandas()






