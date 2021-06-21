# -*-coding:utf-8-*-
# @Time    : 2019/6/3 0003 10:56
# @Author   :zhuxinquan
# @File    : mysql_02.py

import pymysql
import pandas as pd


def creat_biao(mysql_command):
    # print("建立表")
    conn = pymysql.connect(host="192.168.2.159", user ="developer", password ="developer123", database="public_data_2", charset ="utf8")
    cursor = conn.cursor()

    # print(conn)
    # print("链接成功")
    # mysql_command = "Create table `public_data`.`finance1`(`name_first` varchar(30) NOT NULL,`province` text,`frequency` text,`statistic_units` text,`first_record` time,`last_record` time,`pjs` varchar(30),`fc` varchar(30),`bzc` varchar(30),`pd` varchar(30),`fd` varchar(30),`byxs` varchar(30),`max` varchar(30),`min` varchar(30),`mid` varchar(30),`num_record` varchar(30)," \
    #                 "`1947` varchar(30),`1948` varchar(30),`1949` varchar(30),`1950` varchar(30),`1951` varchar(30),`1952` varchar(30),`1953` varchar(30),`1954` varchar(30),`1955` varchar(30),`1956` varchar(30),`1957` varchar(30),`1958` varchar(30),`1959` varchar(30),`1960` varchar(30),`1961` varchar(30),`1962` varchar(30),`1963` varchar(30),`1964` varchar(30),`1965` varchar(30),`1966` varchar(30),`1967` varchar(30),`1968` varchar(30),`1969` varchar(30),`1970` varchar(30),`1971` varchar(30),`1972` varchar(30), `1973` varchar(30),`1974` varchar(30),`1975` varchar(30),`1976` varchar(30),`1977` varchar(30),`1978` varchar(30),`1979` varchar(30),`1980` varchar(30),`1981` varchar(30),`1982` varchar(30),`1983` varchar(30),`1984` varchar(30),`1985` varchar(30),`1986` varchar(30),`1987` varchar(30),`1988` varchar(30),`1989` varchar(30),`1990` varchar(30),`1991` varchar(30),`1992` varchar(30),`1993` varchar(30),`1994` varchar(30),`1995` varchar(30),`1996` varchar(30),`1997` varchar(30),`1998` varchar(30),`1999` varchar(30),`2000` varchar(30),`2001` varchar(30),`2002` varchar(30),`2003` varchar(30),`2004` varchar(30),`2005` varchar(30),`2006` varchar(30),`2007` varchar(30), `2008` varchar(30),`2009` varchar(30),`2010` varchar(30),`2011` varchar(30),`2012` varchar(30),`2013` varchar(30),`2014` varchar(30),`2015` varchar(30),`2016` varchar(30),`2017` varchar(30),`2018` varchar(30),`2019` varchar(30),primary key (`name_first`))"
    print(mysql_command)

    effect_row = cursor.execute(mysql_command)
    row_result = cursor.fetchall()
    # print(row_result)
    cursor.close()
    conn.close()


def insert_data(mysql_command):
    conn = pymysql.connect(host="192.168.2.159", user="developer", password="developer123", database="public_data",
                           charset="utf8")
    cursor = conn.cursor()

    # mysql_command = "INSERT INTO `public_data`.`finance2`(name_first,区域) VALUES (\"{0}\",\"{1}\" )".format("zhuxinquan4","jhahhahaha")
    # print(mysql_command)

    effect_row = cursor.execute(mysql_command)
    row_result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    # print("成功")
    # print()


def insert_data_2(mysql_command):
    print()


def creat_biao_2(mysql_command):
    print()


my_dict = {
"统计名称":"name_first",
"区域":"QY",
"次国家":"CGJ",
"频率":"PL",
"单位":"DW",
"数据来源":"SJLY",
"状态":"ZT",
"数列ID":"SL_ID",
"SR码":"SR_M",
"助记符":"ZJF",
"函数信息":"HSXX",
"首次观测日期":"SCGCRQ",
"最后观测日期":"ZHGCRQ",
"最后更新时间":"ZHGXSJ",
"数列备注":"SLBZ",
"您可以":"NKY",
"平均":"PJ",
"方差":"FC",
"标准差":"PZC",
"偏度":"PD",
"峰度":"FD",
"变异系数":"BYXS",
"最小":"ZX",
"最大":"ZD",
"中位数":"ZWS",
"观测次数":"GCCS",
"数据来源_表":"from_table"
}


def read_data_from_pandas(myaddress, myname):
    print("读取数据")

    mydata = pd.read_excel(myaddress, dtype = 'str')
    mark_local = 0
    mylist_all = []

    mydata = mydata.fillna(0)
    field_list = []

    # 获取数据
    for index, row in mydata.iteritems():
        if mark_local == 0:     # 设置字典
            for i in range(len(row)):
                if i>=17:
                    row[i] = row[i].replace("-", '_')[0:7]        # 月的
                    # row[i] = row[i].replace("-", '_')[0:7]
                    "dada".replace("-", '')
                # print(i, row[i])
                field_list.append(row[i])
        else:
            mylist = [index]
            mylist.extend(list(row))
            mylist_all.append(mylist)
        mark_local += 1

    # 插入数据1
    insert_sql = "INSERT INTO `public_data`.`{}`(name_first,".format("public_all")
    for i in field_list[0:25]:
        t = my_dict[i] + ','
        insert_sql += t
    insert_sql += "from_table,"
    insert_sql = insert_sql[0:-1] + ") VALUES ("
    # print(insert_sql)
    print("插入数据1")
    for t_i in mylist_all:
        insert_sql1 = insert_sql
        # print(t_i)
        for one in t_i[0:26]:
            # print(one)
            if str(one) == "nan":
                one = "NULL"
                tmp = str(one)+","
                insert_sql1 += tmp
            else:
                tmp = "\"" + str(one) + "\"" + ","
                insert_sql1 += tmp


        insert_sql1 += "\""+myname+"\""+","
        insert_sql1 = insert_sql1[0:-1]+")"
        try:
            insert_data(insert_sql1)
        except:
            print("出错")
            print(insert_sql1)
            # exit()

    print("插入数据2")
    for t_i in mylist_all:
        for one in range(26, len(t_i) - 1):
            # print(field_list[one], t_i[one])
            t1= field_list[one]
            t2 = t_i[one]
            if t1 == 'nan' and t2 == 'nan':
                t1 = 'NULL'
                t2 = "NULL"
                insert_sql = "INSERT INTO `public_data`.`public_all_date` (name_first, GCSJ,my_VALUES) VALUES (\'{0}\',{1},{2})".format(t_i[0], t1, t2)
            elif t1 == 'nan' and t2 != 'nan':
                t1 = 'NULL'
                insert_sql = "INSERT INTO `public_data`.`public_all_date` (name_first, GCSJ,my_VALUES) VALUES (\'{0}\',{1},\'{2}\')".format(t_i[0], t1, t2)

            elif t1 != 'nan' and t2 == 'nan':
                t2 = 'NULL'
                insert_sql = "INSERT INTO `public_data`.`public_all_date` (name_first, GCSJ,my_VALUES) VALUES (\'{0}\',\'{1}\',{2})".format(
                    t_i[0], t1, t2)
            else:
                insert_sql = "INSERT INTO `public_data`.`public_all_date` (name_first, GCSJ,my_VALUES) VALUES (\'{0}\',\'{1}\',\'{2}\')".format(
                    t_i[0], t1, t2)

            try:
                insert_data(insert_sql)
            except:
                print("出错")
                print(insert_sql)
                # exit()
    #     # exit()

def travel_data():
    import glob
    # myfile_path = glob.glob(r"C:\Users\Administrator\Desktop\1111\all\*.xlsx")
    # "C:\Users\Administrator\Desktop\比较特殊"
    myfile_path = glob.glob(r"C:\Users\Administrator\Desktop\比较特殊\*.xlsx")
    for i in myfile_path:
        print(i)
        i_name = i.replace(' ', '_')
        i_name = i_name.replace('-', '_')
        # print(i_name)
        myname = i_name.split('\\')[-1].split('.')[0]
        print(myname)
        print()
        read_data_from_pandas(i, myname)
        # exit()

if __name__ == '__main__':
    # read_data_from_pandas()
    # insert_data()
    travel_data()
