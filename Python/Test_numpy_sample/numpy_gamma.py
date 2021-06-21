# -*-coding:utf-8-*-
# @Time    : 2019/12/10 0010 17:04
# @Author  :zhu
# @File    : numpy_gamma.py
# @task description :


#需要导入的库
import numpy as np
import Example_matplotlib.pyplot as plt
import scipy.special as sps

shape, scale = 2., 2.
s = np.random.gamma(shape, scale, 1000)     # 在2.到2.之间随机生成1000个小数
print(s)
exit()

count, bins, ignored = plt.hist(s, 50, normed=True)     # 50：是50个条形图
'''
根据伽马分布的概率密度
伽马分布常被用来模拟电子元件的失效时间，
并且在泊松分布事件之间的等待时间相关的过程中自然产生。
'''
y=bins**(shape-1)*(np.exp(-bins/scale)/(sps.gamma(shape)*scale**shape))
plt.plot(bins, y , linewidth=2, color='r')
plt.show()
