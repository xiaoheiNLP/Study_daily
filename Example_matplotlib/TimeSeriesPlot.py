# -*-coding:utf-8-*-
# @Time    : 2019/12/12 0012 15:48
# @Author  :zhu
# @File    : TimeSeriesPlot.py
# @task description :
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(25, 10), dpi=300)
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']     # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False      # 解决保存图像是负号'-'显示为方块的问题
mydata = pd.read_csv("./data/data1.csv")
y1 = list(mydata["value1"])[0:105]
y2 = list(mydata["value2"])[0:105]
print(y1)
print(y2)


ax = plt.subplot(111)
plt.xticks(np.arange(0, len(y2), step=2))
# t1 = np.arange(0, 105, 1)

t1 = [i for i in range(len(y2))]

for n in [y1, y2]:
    plt.plot(t1, n, label="n=%d"%(1,))

leg = plt.legend(loc='best', ncol=2, shadow=False, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.title("核心模型模拟结果图")
plt.savefig("./data/核心模型模拟结果图.png", dpi=200)
# plt.show()