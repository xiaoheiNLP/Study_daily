# -*-coding:utf-8-*-
# @Time    : 2019/10/30 0030 15:15
# @Author  :zhu
# @File    : lazy_load.py
# @task description :


class cached_property(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value

class Test(object):
    def __init__(self, value):
        self.value = value;
    @cached_property
    def display(self):
        print("some complicated compute here")
        return self.value

if __name__ == '__main__':
    t = Test(1000)
    print(t.display)

    print(t.display)
