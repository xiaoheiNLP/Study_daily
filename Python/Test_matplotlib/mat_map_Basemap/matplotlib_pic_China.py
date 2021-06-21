# -*-coding:utf-8-*-
# @Time    : 2019/6/18 0018 13:53
# @Author   :zhuxinquan
# @File    : matplotlib_pic_China.py


import Example_matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from Example_matplotlib.patches import Polygon

plt.figure(figsize=(16, 8))
m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100)
m.drawcoastlines()          # 画上海岸线
m.drawcountries(linewidth=1.5)      # 画上国家

# 画上行政区
CHN = r'C:\Users\Administrator\Desktop\MyProject\Test_module\Test_matplotlib\data_base'
m.readshapefile(CHN+r'\gadm36_CHN_shp\gadm36_CHN_1', 'states', drawbounds=True)    # 加省界

# 上色
ax = plt.gca()
for nshape, seg in enumerate(m.states):

    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)

# 画上台湾省
m.readshapefile(CHN + '\gadm36_TWN_shp\gadm36_TWN_1', 'taiwan', drawbounds=True)
for nshape, seg in enumerate(m.taiwan):
    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)

for shapedict in m.states_info:
    statename = shapedict['NL_NAME_1']
    p = statename.split('|')
    if len(p) > 1:
        s = p[1]
    else:
        s = p[0]
        print(s)

# for shapedict in m.taiwan_info:
#
#     s = shapedict['NAME_CHINE']
#     print(s)


plt.title(r'$祝鑫泉画的World\ Map$', fontsize=24)
plt.show()

