# -*-coding:utf-8-*-

"""
冒泡排序实现
"""


def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] < lst[j+1]:
                # tmp = lst[j]
                # lst[j] = lst[j+1]
                # lst[j+1] = tmp
                (lst[j], lst[j+1]) = (lst[j+1], lst[j])
    return lst




if __name__ == '__main__':
    print("实现冒泡排序")
    print(bubbleSort([1, 4, 6, 5, 2, 8, 7, 9]))

    # t = [1, 4, 6, 5, 2, 8, 7, 9]
    # print(len(t))
    # print(t[8])


"""
百级排序消耗时间： 0.002630949020385742
千级排序消耗时间： 0.23256206512451172
万级排序消耗时间： 23.112180948257446
"""