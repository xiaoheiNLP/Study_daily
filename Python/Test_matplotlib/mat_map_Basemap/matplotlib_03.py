# -*-coding:utf-8-*-
# @Time    : 2019/6/18 0018 16:13
# @Author   :zhuxinquan
# @File    : matplotlib_03.py


from mpl_toolkits.basemap import Basemap
import Example_matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(20, 10))  # 长和宽
map = Basemap(projection='ortho',
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#cc9955', lake_color='aqua')
map.drawcoastlines()

lon = 50.4
lat = 1.4

x, y = map(lon, lat)

plt.text(x, y, '哈哈哈哈哈哈哈',fontsize=12,fontweight='bold',
                    ha='left',va='bottom',color='r')

lon = 2.1
lat = 41.

x, y = map(lon, lat)

plt.text(x, y, 'Barcelona',fontsize=12,fontweight='bold',
                    ha='left',va='center',color='k',
                    bbox=dict(facecolor='b', alpha=0.2))
plt.show()