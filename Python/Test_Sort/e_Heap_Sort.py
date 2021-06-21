# -*-coding:utf-8-*-

"""
堆排序实现
"""

def heapSort(lst):
    def heapadjust(arr, start, end):  # 将以start为根节点的堆调整为大顶堆
        temp = arr[start]
        son = 2*start+1
        while son <= end:
            if son < end and arr[son] < arr[son+1]:  # 找出左右孩子节点较大的
                son += 1
            if temp >= arr[son]:       # 判断是否为大顶堆
                break
            arr[start] = arr[son]     # 子节点上移
            start = son               # 继续向下比较
            son = 2*son+1

        arr[start] = temp             # 将原堆顶插入正确位置

    n = len(lst)
    # 建立大顶堆
    root = n//2-1    # 最后一个非叶节点（完全二叉树中）

    # 构建最大堆
    while(root >= 0):
        heapadjust(lst, root, n-1)
        root -= 1

    # 掐掉堆顶后调整堆
    i = n-1
    while(i >= 0):
        # print(lst[0])
        (lst[0], lst[i]) = (lst[i], lst[0])  # 将大顶堆堆顶数放到最后
        heapadjust(lst, 0, i-1)    # 调整剩余数组成的堆
        i -= 1
    return lst


if __name__ == '__main__':
    print("实现堆排序")
    print(heapSort([10, 1, 4, 6, 5, 2, 8, 8, 7, 9, 3]))

