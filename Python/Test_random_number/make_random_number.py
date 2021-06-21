# -*-coding:utf-8-*-
# @Time    : 2019/7/1 0001 10:47
# @Author   :zhuxinquan
# @File    : make_random_number.py

"""
产生各种随机数的各种方式

"""


# random模块
def test_random_random():
    import random
    print(random.randint(0, 99))    # 随机产生一个0到99的整数
    print()
    print(random.randrange(0, 100, 1))      # 随机产生一个0到100的奇数
    print(random.randrange(0, 100, 2))      # 随机产生一个0到100的偶数,1和2是步长的意思
    exit()
    print()
    print(random.uniform(1, 10))      # 随机产生一个1到10的浮点数
    print()
    print(random.choice('abcdefg&#%^*f'))      # 随机抽取字符串中的一个字符
    print(random.sample('abcdefghij', 3))       # 随机从字符串中抽取3字符，产生list
    print(random.sample([1, 2, 3, 4, 5, 6, 7, 8], 4))
    print()

    items = [1, 2, 3, 4, 5, 6]
    random.shuffle(items)       # 打乱，洗牌,作用在本身上，不需要迭代
    print(items)

    print()
    rs = random.sample(range(1, 10), 100)
    print(rs)


"""
    阶段总结：
        1.random模块还是很low，不是很强大
        2.在速度上，还没多次测试，就已经
        3.还得用numpy
"""


# numpy模块生成随机数
def test_random_numpy():
    import numpy as np

    # 生成一个正态分布，括号里的参数是生成随机数的维度
    t1 = np.random.randn(3, 4)

    # 参数见源码，需要提醒的是这个函数是允许出现重复的（可放回抽样）
    t2 = np.random.randint(0, 10, 10)

    # 产生一个正太分布:loc是正态分布的均值，scale是正态分布的标准差，返回的是正态分布中产生的随机数，个数可以调整
    t3 = np.random.normal(loc=1, scale=2)

    # 产生一个均匀分布：定义上界和下界，
    t4 = np.random.uniform(0, 10, 2)
    print(t4)


def main_test():
    print("主要测试")
    import numpy as np
    s = np.random.uniform(1, 2, 1000)
    # print(np.all(s >= 2))
    # print(s)
    # exit()

    import Example_matplotlib.pyplot as plt
    count, bins, ignored = plt.hist(s, 15, density=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.show()


if __name__ == '__main__':
    # test_random_random()      # 测试Python自带的random包
    # test_random_numpy()     # 测试numpy中的随机函数包
    main_test()

