# -*-coding:utf-8-*-
# @Time    : 2019/9/3 0003 15:23
# @Author  :zhu
# @File    : travel_main_a.py
# @task description :

from Test_log.mylog import LogMgr
import time


if __name__ == '__main__':
    log_mgr = LogMgr("Cmylog1.log")
    for i in range(10000000):
        print(i)
        log_mgr.info(u"Hellow World A {}".format(i))
        time.sleep(0.1)

