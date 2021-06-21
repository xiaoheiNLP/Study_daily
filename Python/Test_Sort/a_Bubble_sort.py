# -*-coding:utf-8-*-

"""
冒泡排序实现
"""


def bubbleSort(lst):
    n = len(lst)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                (lst[j], lst[j+1]) = (lst[j+1], lst[j])

    return lst


if __name__ == '__main__':
    print("实现冒泡排序")
    print(bubbleSort([1, 4, 6, 5, 2, 8, 7, 9]))




"""
冒泡的测试时间概览：

百级排序消耗时间： 0.002513885498046875
千级排序消耗时间： 0.24237895011901855
万级排序消耗时间： 23.623369932174683
十万级排序消耗时间：10分钟没跑好,可能要到天亮
"""
