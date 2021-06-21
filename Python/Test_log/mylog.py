# -*-coding:utf-8-*-
# @Time    : 2019/9/3 0003 15:15
# @Author  :zhu
# @File    : mylog.py
# @task description :

import logging
import logging.handlers


class LogMgr:
    def __init__(self, logpath):
        self.LOG = logging.getLogger('log')
        # loghdlr1 = logging.handlers.RotatingFileHandler(logpath, "a", 0, 1)
        loghdlr1 = logging.handlers.TimedRotatingFileHandler("./logs/"+logpath, when='M', interval=1, backupCount=5)
        fmt1 = logging.Formatter("%(asctime)s %(threadName)-10s %(message)s", "%Y-%m-%d %H:%M:%S")
        loghdlr1.setFormatter(fmt1)
        self.LOG.addHandler(loghdlr1)
        self.LOG.setLevel(logging.INFO)

        # self.MARK = logging.getLogger('mark')
        # loghdlr2 = logging.handlers.RotatingFileHandler(markpath, "a", 0, 1)
        # fmt2 = logging.Formatter("%(message)s")
        # loghdlr2.setFormatter(fmt2)
        # self.MARK.addHandler(loghdlr2)
        # self.MARK.setLevel(logging.INFO)

    def error(self, msg):
        if self.LOG is not None:
            self.LOG.error(msg)

    def info(self, msg):
        if self.LOG is not None:
            self.LOG.info(msg)

    def debug(self, msg):
        if self.LOG is not None:
            self.LOG.debug(msg)

    def mark(self, msg):
        if self.MARK is not None:
            self.MARK.info(msg)


if __name__ == "__main__":
    pass



"""
学习网站：
https://www.cnblogs.com/jiyanjiao-702521/p/9597985.html
https://blog.csdn.net/gammag/article/details/49943553

"""