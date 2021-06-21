# -*-coding:utf-8-*-
# @Time    : 2019/10/23 0023 11:33
# @Author  :zhu
# @File    : pysnooper_1.py
# @task description :

import pysnooper

@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []

        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


@pysnooper.snoop()
def cal_num():
    for i in range(7):
        print(i)

    return "zhu"

if __name__ == '__main__':
    print(cal_num())
