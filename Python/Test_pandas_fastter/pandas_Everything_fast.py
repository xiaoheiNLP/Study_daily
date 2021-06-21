# -*-coding:utf-8-*-
# @Time    : 2019/11/15 0015 13:42
# @Author  :zhu
# @File    : pandas_Everything_fast.py
# @task description :
"""
续上之前的，这里主要讲速度的提升
"""
import pandas as pd
import time

"""测试一"""
def soc_loop(df, team=str):
    t1 = time.time()
    df["Draws"] = 9999

    for row in range(len(df)):
        if (df["对手"].iloc[row] == team) & (df["得分"].iloc[row] == "27"):
            df["Draws"].iloc[row] = "Draw"
        else:
            df["Draws"].iloc[row] = "No_Draw"

    print("消耗时间是：", time.time() - t1)
    return df

def main_test1():
    df = pd.read_excel("./hadeng.xlsx")
    df_1 = soc_loop(df=df, team="勇士")
    print(df_1.head(5))


"""测试二"""
def soc_iter(myname, Team, score, T_score):
    """
    匹配名字和得分
    :param myname:
    :param Team:
    :param score:
    :param T_score:
    :return:
    """
    r1 = (Team == myname)
    r2 = (score == T_score)
    return (r1 & r2)


def main_test2():
    df = pd.read_excel("./hadeng.xlsx")
    draw_series = []
    t1 = time.time()
    for index, row in df.iterrows():
        draw_series.append(soc_iter(row["对手"], row["得分"]))
    df["Draw"] = draw_series
    print("消耗时间是", time.time() - t1)
    df.to_excel("./result/James_Harden.xlsx")


"""测试三"""
def main_test3():
    df = pd.read_excel("./hadeng.xlsx")
    t1 = time.time()
    df["Draws"] = df.apply(lambda row: soc_iter(row["对手"], row["得分"]), axis=1)
    print("消耗时间是：", time.time() - t1)
    df.to_excel("./result/james_Harden2.xlsx", index=False)

"""测试四"""
def main_test4():
    df = pd.read_excel("./hadeng.xlsx")
    t1 = time.time()
    df["Draws"] = soc_iter(df["对手"], df["得分"])
    print("消耗时间是：", time.time() - t1)
    df.to_excel("./result/james_Harden4.xlsx", index=False)


"""测试五"""
def main_test5(t = list):
    df = pd.read_excel("./hadeng.xlsx")
    t1 = time.time()
    df["Draws"] = "No_Draws"
    reult = soc_iter("勇士", df["对手"].values, df["得分"].values, 27)
    print(reult)
    print(len(reult))
    reult = list(reult)
    print(reult.count(True))
    df.loc[reult, "Draws"] = ["Draws" for _ in range(539)]
    print("消耗时间是：", time.time() - t1)
    # df.to_excel("./result/james_Harden5.xlsx", index=False)

if __name__ == '__main__':

    main_test5()





"""
测试一：用for循环和iloc函数，消耗时间是：136.42s
测试二：用iterrows，        消耗时间是：0.8946373462677002
测试三：用apply             消耗时间是：0.2473592
测试四：不成功：不需要成功了，就是利用逻辑运算
测试五：用numpy以及loc取值函数             消耗时间是：0.003989219665527344
总结：用量化的数据，比循环快太多，所以以后需要大量遍历的数据但可采用这种方式
"""