# -*-coding:utf-8-*-

"""
选择排序实现
"""



def selectSort(mylist):
    for i in range(len(mylist)):
        min_index = i
        for j in range(i, len(mylist)):
            if mylist[j] < mylist[min_index]:
                min_index = j
        # mylist[i] = mylist[min_index]
        (mylist[i], mylist[min_index]) = (mylist[min_index], mylist[i])
    return mylist






if __name__ == '__main__':
    print(selectSort([10, 1, 4, 4, 6, 5, 2, 8, 7, 9, 9]))




"""
选择的测试时间概览：

百级排序消耗时间： 0.0015599727630615234
千级排序消耗时间： 0.12975192070007324
万级排序消耗时间： 12.949650049209595
十万级排序消耗时间：跟冒泡一样，跑得我的电脑发烫了，还没跑完，果断stop
"""
