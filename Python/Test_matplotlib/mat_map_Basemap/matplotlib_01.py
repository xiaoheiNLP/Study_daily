# -*-coding:utf-8-*-
# @Time    : 2019/6/18 0018 10:58
# @Author   :zhuxinquan
# @File    : matplotlib_01.py


import Example_matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.figure(1)
# map=Basemap()
map=Basemap(llcrnrlon=70, llcrnrlat=3, urcrnrlon=139, urcrnrlat=54)     # 画中国 经135度2分30秒-东经73度40分，北纬3度52分-北纬53度33分
map.drawcoastlines()
map.drawcountries()         # 加海岸线
# map.drawrivers(color='blue', linewidth=0.3)  # 加河流
CHN = r"C:\Users\Administrator\Downloads"
map.readshapefile(CHN+r'\gadm36_CHN_shp\gadm36_CHN_1', 'states', drawbounds=True)    # 加省界
# map.readshapefile(CHN+r'\gadm36_TWN_shp\gadm36_TWN_1', 'taiwan', drawbounds=True)    # 加台湾

plt.title(r'$World\ Map$', fontsize=24)
plt.show()