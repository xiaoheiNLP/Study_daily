# -*-coding:utf-8-*-
# @Time    : 2019/6/19 0019 15:32
# @Author   :zhuxinquan
# @File    : echarts_01.py

"""
画中国地图，Basemap就是垃圾


"""

from pyecharts.charts import Map
from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
# from pyecharts.globals import ChartType, SymbolTyp


def geo_base() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-基本示例"),
        )
    )
    return c


def read_csv():
    fopen = open(r"C:\Users\Administrator\Desktop\result_map2.csv", 'r')
    mydata = fopen.readlines()
    result_map = []
    for line in mydata[1:]:
        line = line.strip()
        line_list = line.split(',')
        print(line_list)
        tmp_province = line_list[0].replace('省', '')
        tmp_province = tmp_province.replace("市", '')
        tmp_sick = line_list[1]

        tmp_sick_num = round(float(line_list[2]), 2)
        if "自治区" in tmp_province:
            tmp_province = tmp_province[0:2]
        result_map.append([tmp_province, tmp_sick_num])
    print(result_map)
    return result_map


def map_visualmap() -> Map:

    t = read_csv()
    c = (
        Map()
        .add("每10w人中胃癌患者数量", t, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="每10w人中胃癌患者数量"),
            visualmap_opts=opts.VisualMapOpts(max_=160, is_piecewise=True),
        )
    )
    return c


if __name__ == '__main__':

    # read_csv()


    T = map_visualmap()
    T.is_map_symbol_show = True
    T.options["width"] = "900px"
    # T.options["height"] = "900px"
    # T.width = 1000
    # T.height = 1000
    T.render('hahha1.html')
