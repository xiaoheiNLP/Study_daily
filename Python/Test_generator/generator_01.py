# -*-coding:utf-8-*-
# @Time    : 2019/6/26 0026 9:39
# @Author   :zhuxinquan
# @File    : generator_01.py

def test_generator():
    # fibonacci数列
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            a, b = b, a + b
            n = n + 1
            print(a)
        return 'done'

    a = fib(10)
    # print(a)
    print(fib(10))


if __name__ == '__main__':
    test_generator()


