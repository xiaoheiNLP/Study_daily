# -*-coding:utf-8-*-

"""
堆排序实现
"""

def heapSort(lst):
    def func1(arr, start, end):     # 形成最大堆

        tmp = arr[start]
        son = start * 2 + 1
        while son < end:    #

            if son < end and arr[son] < arr[son + 1]:
                son += 1
            if tmp >= arr[son]:
                break
            arr[start] = arr[son]   # 父节点
            start = son
            son = son * 2 + 1
        arr[start] = tmp



    n = len(lst)
    root = n//2 - 1     # 非叶节点
    #
    while(root >= 0 ):
        func1(lst, root, n -1)
        root -= 1

    i = n -1

    while i >= 0:

        (lst[0], lst[i]) = (lst[i], lst[0])
        func1(lst, 0, i - 1)

        i -= 1

    return lst


if __name__ == '__main__':
    print("实现堆排序")
    print(heapSort([10, 1, 4, 6, 5, 2, 8, 8, 7, 9, 3]))
