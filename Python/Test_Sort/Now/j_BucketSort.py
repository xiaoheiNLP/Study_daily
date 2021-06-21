# -*-coding:utf-8-*-
"""
桶排序实现
"""

def bucketSort(lst):
    # 桶内使用快速排序
    def QuickSort(lst):
        def partition(arr, left, right):
            key = left  # 划分参考数索引,默认为第一个数，可优化
            while left < right:
                while left < right and arr[right] >= arr[key]:
                    right -= 1
                while left < right and arr[left] <= arr[key]:
                    left += 1
                (arr[left], arr[right]) = (arr[right], arr[left])
            (arr[left], arr[key]) = (arr[key], arr[left])
            return left

        def quicksort(arr, left, right):  # 递归调用
            if left >= right:
                return
            mid = partition(arr, left, right)
            quicksort(arr, left, mid - 1)
            quicksort(arr, mid + 1, right)

        # 主函数
        n = len(lst)
        if n <= 1:
            return lst
        quicksort(lst, 0, n - 1)
        return lst

    n = len(lst)
    big = max(lst)
    num = big // 10 + 1
    bucket = []
    buckets = [[] for i in range(0, num)]
    for i in lst:
        buckets[i // 10].append(i)  # 划分桶
    for i in buckets:  # 桶内排序
        bucket = QuickSort(i)
    arr = []
    for i in buckets:
        if isinstance(i, list):
            for j in i:
                arr.append(j)
        else:
            arr.append(i)
    for i in range(0, n):
        lst[i] = arr[i]
    return lst


if __name__ == '__main__':
    print("桶排序")
    print(bucketSort([1, 4, 6, 5, 2, 8, 7, 9]))

