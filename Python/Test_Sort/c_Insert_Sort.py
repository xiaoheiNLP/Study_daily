# -*-coding:utf-8-*-

"""
插入排序实现
"""

def insertSort(lst):
    n = len(lst)
    for i in range(1, n):
        j = i
        target = lst[i]  # 每次循环的一个待插入的数
        while j > 0 and target < lst[j - 1]:  # 比较、后移，给target腾位置
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = target  # 把target插到空位
    return lst


if __name__ == '__main__':
    print("实现插入排序")
    print(insertSort([1, 4, 6, 5, 2, 8, 7, 9]))

"""
插入的测试时间概览：

百级排序消耗时间： 0.0009980201721191406
千级排序消耗时间： 0.11395096778869629
万级排序消耗时间： 10.810659170150757
十万级排序消耗时间： 五分钟没跑好，等能肯定的是比冒泡快

"""