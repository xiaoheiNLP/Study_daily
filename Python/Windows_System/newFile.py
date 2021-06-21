# -*-coding:utf-8-*-
# @Time    : 2019/12/17 0017 13:57
# @Author  :zhu
# @File    : newFile.py
# @task description :
"""
Python完成一些python的系统操作
"""
import os

"""创建文件夹"""
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")

def removeFile():
    dirPath = r"C:\Users\Administrator\Desktop\MyProject\Study_daily\Python\Windows_System"
    print('移除前test目录下有文件：%s' %os.listdir(dirPath))

    # 判断文件是否存在
    print(dirPath+"\\foo.txt")
    if(os.path.exists(dirPath+"\\foo.txt")):
        os.remove(dirPath+"\\foo.txt")
        print('移除后test 目录下有文件：%s' %os.listdir(dirPath))
    else:
        print("要删除的文件不存在！")


if __name__ == '__main__':
    # testPath = r"C:\Users\Administrator\Desktop\MyProject\Study_daily\Python\Windows_Systemzhu"
    # mkdir(testPath)
    removeFile()


