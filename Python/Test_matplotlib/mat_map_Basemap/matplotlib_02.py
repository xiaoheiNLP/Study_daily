# -*-coding:utf-8-*-
# @Time    : 2019/6/18 0018 15:25
# @Author   :zhuxinquan
# @File    : matplotlib_02.py


def make_data():
    import pandas as pd
    df = pd.read_excel(r'C:\Users\Administrator\Desktop\MyProject\Test_module\Test_matplotlib\data_base\data\A0101a.xls', encoding='utf-8', head=None, skiprows=6)
    df.head()

    df[['省份', '人口数']]= df[['Unnamed: 0', 'Unnamed: 4']]
    df = df['省份'].to_frame().join(df['人口数'])
    df = df[1:]
    df['省名'] = df['省份'].str.replace(' ', '')
    df.set_index('省名', inplace = True)
    del df['省份']
    df.to_csv('./data_base/data/chnpop.csv')


def pic_map():
    import numpy as np
    import pandas as pd
    import Example_matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap
    from Example_matplotlib.patches import Polygon
    from Example_matplotlib.colors import rgb2hex
    from Example_matplotlib.collections import PatchCollection
    from Example_matplotlib import pylab

    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(20, 10))     # 长和宽
    # m= Basemap(llcrnrlon=73, llcrnrlat=18, urcrnrlon=135, urcrnrlat=55) #指定中国的经纬度
    m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51,
                projection='lcc', lat_1=33, lat_2=45, lon_0=100)  # ‘lcc'将投影方式设置为兰伯特投影
    # projection='ortho' # 投影方式设置为正投影——类似地球仪

    CHN = r'C:\Users\Administrator\Desktop\MyProject\Test_module\Test_matplotlib\data_base'
    m.readshapefile(CHN + r'\gadm36_CHN_shp\gadm36_CHN_1', 'states', drawbounds=True)  # 加省界

    # 读取数据
    df = pd.read_csv('./data_base/data/chnpop.csv')
    df['省名'] = df.省名.str[:2]
    df.set_index('省名', inplace=True)

    # 把每个省的数据映射到colormap上
    statenames = []
    colors = {}
    patches = []
    cmap = plt.cm.YlOrRd  # 国旗色红黄色调
    vmax = 10 ** 8
    vmin = 3 * 10 ** 6

    # 处理地图包里的省名
    for shapedict in m.states_info:
        statename = shapedict['NL_NAME_1']
        p = statename.split('|')
        if len(p) > 1:
            s = p[1]
        else:
            s = p[0]
        s = s[:2]
        if s == '黑龍':
            s = '黑龙'
        statenames.append(s)
        pop = df['人口数'][s]
        colors[s] = cmap(np.sqrt((pop - vmin) / (vmax - vmin)))[:3]  # 根据归一化后的人口数映射颜色
    # exit()
    ax = plt.gca()
    for nshape, seg in enumerate(m.states):
        color = rgb2hex(colors[statenames[nshape]])
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        patches.append(poly)
        ax.add_patch(poly)

    # 图片绘制加上台湾（台湾不可或缺）
    m.readshapefile(CHN + '\gadm36_TWN_shp\gadm36_TWN_1', 'taiwan', drawbounds=True)
    for nshape, seg in enumerate(m.taiwan):
        poly = Polygon(seg, facecolor='w')
        patches.append(poly)
        ax.add_patch(poly)

    # 添加colorbar 渐变色legend
    colors1 = [i[1] for i in colors.values()]
    colorVotes = plt.cm.YlOrRd
    p = PatchCollection(patches, cmap=colorVotes)
    p.set_array(np.array(colors1))
    pylab.colorbar(p)



    #4266831.094478747, 1662846.3046657
    lon = 4097273.638675578
    lat = 4008859.232616643
    x, y = m(lon, lat)

    plt.text(x, y, '国都', fontsize=120, fontweight='bold',
             ha='left', va='bottom', color='k')

    m.scatter(x, y, s=200, marker='*', facecolors='r', edgecolors='B')  # 绘制首都

    plt.title(u'祝鑫泉画的World  Map ', fontsize=24)
    plt.savefig("./data_base/result/Chinese_Map1.png", dpi=100)  # 指定分辨率
    plt.show()


if __name__ == '__main__':
    pic_map()

