# -*-coding:utf-8-*-

"""
归并排序实现
"""

def mergeSort(lst):
    # 合并左右子序列函数
    def merge(arr, left, mid, right):
        temp = []  # 中间数组
        i = left  # 左段子序列起始
        j = mid + 1  # 右段子序列起始
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for i in range(left, right + 1):  # !注意这里，不能直接arr=temp,他俩大小都不一定一样
            arr[i] = temp[i - left]

    # 递归调用归并排序
    def mSort(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mSort(arr, left, mid)
        mSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    n = len(lst)
    mSort(lst, 0, n - 1)
    return lst

if __name__ == '__main__':
    print("实现归并排序")
    print(mergeSort([1, 4, 6, 5, 2, 8, 7, 9]))

