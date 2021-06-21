# -*-coding:utf-8-*-

"""
选择排序实现
"""



def selectSort(ls):
    n = len(ls)
    for i in range(0, n):
        minIndex = i
        for j in range(i + 1, n):   # 比较一遍，记录索引不交换
            if ls[j] < ls[minIndex]:    # 记录索引
                minIndex = j
        if minIndex != i:   # 按索引交换
            (ls[minIndex], ls[i]) = (ls[i], ls[minIndex])
    return ls






if __name__ == '__main__':
    print(selectSort([1, 4, 4, 6, 5, 2, 8, 7, 9, 9]))




"""
选择的测试时间概览：

百级排序消耗时间： 0.0015599727630615234
千级排序消耗时间： 0.12975192070007324
万级排序消耗时间： 12.949650049209595
十万级排序消耗时间：跟冒泡一样，跑得我的电脑发烫了，还没跑完，果断stop
"""
