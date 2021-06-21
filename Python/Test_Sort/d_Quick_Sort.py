# -*-coding:utf-8-*-

"""
快速排序实现
"""



def quickSort(lst):
    # 此函数完成分区操作
    def partition(arr, left, right):
        key = left  # 划分参考数索引,默认为第一个数为基准数，可优化
        while left < right:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1

            # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left += 1
            # 此时已找到一个比基准大的书，和一个比基准小的数，将他们互换位置
            (arr[left], arr[right]) = (arr[right], arr[left])

        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
        (arr[left], arr[key]) = (arr[key], arr[left])
        # 返回目前基准所在位置的索引
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return
        # 从基准开始分区
        mid = partition(arr, left, right)
        # 递归调用
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(lst)
    quicksort(lst, 0, n-1)
    return lst


if __name__ == '__main__':
    print("实现快速排序")
    print(quickSort([3, 10, 4, 6, 5, 2, 8, 7, 9]))


"""
快速的测试时间概览：

百级排序消耗时间： 0.00038695335388183594
千级排序消耗时间： 0.006429910659790039
万级排序消耗时间： 0.08614110946655273
十万级排序消耗时间： 1.0215158462524414
"""