# -*-coding:utf-8-*-
# @Time    : 2019/6/19 0019 14:21
# @Author   :zhuxinquan
# @File    : matplotlib_04.py

import time

start = time.clock()
from mpl_toolkits.basemap import Basemap
import Example_matplotlib.pyplot as plt
from Example_matplotlib.patches import Polygon
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False


posi=pd.read_excel(r'C:\Users\Administrator\Desktop\MyProject\Test_module\Test_matplotlib\data_base\data\2015Cities-CHINA.xlsx') #读取中国城市数据
lat = np.array(posi["lat"][0:120])                        # 获取维度之维度值
lon = np.array(posi["lon"][0:120])                        # 获取经度值
pop = np.array(posi["pop"][0:120], dtype=float)

size = (pop/np.max(pop))*100
map = Basemap(llcrnrlon=80.33,
              llcrnrlat=3.01,
              urcrnrlon=138.16,
              urcrnrlat=56.123,
             resolution='h', projection='cass', lat_0 = 42.5, lon_0=120)

CHN = r'C:\Users\Administrator\Desktop\MyProject\Test_module\Test_matplotlib\data_base'
map.readshapefile(CHN + r'\gadm36_CHN_shp\gadm36_CHN_1', 'states', drawbounds=True)

map.etopo()     # 绘制地形图，浮雕样式

map.drawcoastlines()

x, y = map(lon[2], lat[2])  # 北京市坐标，经纬度坐标转换为该map的坐标

a, b = map(lon, lat)

# map.scatter(a, b, s=size)   # 取消注释此行即可获得中国各地区人口分布示意图

map.scatter(x, y, s=200, marker='*', facecolors='r', edgecolors='r')    # 绘制首都
print(x, y)
plt.text(x, y, '哈哈', fontsize=12, fontweight='bold',
                    ha='left', va='bottom', color='r')


end = time.clock()

print(end-start)

plt.show()

