#!/usr/bin/env python3

import time
import logging.handlers

# logging初始化工作
logging.basicConfig()

# myapp的初始化工作
myapp = logging.getLogger('myapp')
myapp.setLevel(logging.INFO)

# 添加TimedRotatingFileHandler
# 定义一个1秒换一次log文件的handler
# 保留3个旧log文件
filehandler = logging.handlers.TimedRotatingFileHandler("logs/myapp.log", when='S', interval=1, backupCount=5)
# 设置后缀名称，跟strftime的格式一样  when设置的是S这个结尾必须是S.log
filehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
myapp.addHandler(filehandler)

while True:
    time.sleep(0.1)
    myapp.info("test")