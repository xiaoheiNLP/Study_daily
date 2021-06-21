# -*-coding:utf-8-*-
# @Time    : 2019/12/11 0011 17:17
# @Author  :zhu
# @File    : dict_1.py
# @task description :


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def test():
    mylist = [1, 2, 3, 4, 5]
    print(mylist)
    mydict = dict((enumerate(mylist)))
    print(mydict)


if __name__ == '__main__':

    # 两个字典
    # dict1 = {'a': 10, 'b': 8}
    # dict2 = {'d': 6, 'c': 4, 'a': 11}
    # dict3 = Merge(dict1, dict2)
    # print(dict3)
    test()



