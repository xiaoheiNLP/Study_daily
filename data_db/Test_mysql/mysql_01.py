# -*-coding:utf-8-*-
# @Time    : 2019/5/28 0028 14:55
# @Author   :zhuxinquan
# @File    : mysql_01.py
import pymysql
import pandas as pd


def creat_biao(mysql_command):
    # print("建立表")
    conn = pymysql.connect(host="192.168.2.159", user ="developer", password ="developer123", database="public_data", charset ="utf8")
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
    conn = pymysql.connect(host="192.168.2.159", user="developer", password="developer123", database="public_data_2",
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



def read_data_from_pandas(myaddress, myname):
    print("读取数据")

    mydata = pd.read_excel(myaddress, dtype = 'str')
    mark_local = 0
    mylist_all = []

    mydata = mydata.fillna(0)
    field_list = []

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

    # 建立表
    sql_command_create = "Create table `public_data_2`.`{}`  (`id` int(11) NOT NULL AUTO_INCREMENT,`name_first` varchar(30) NOT NULL,".format(myname)
    # print(sql_command_create)
    # exit()
    for one in range(len(field_list)):
        if one < 7:
            tmp_line = "`{0}` {1},".format(field_list[one], "text")
            sql_command_create += tmp_line
        else:
            tmp_line = "`{0}` {1},".format(field_list[one], "text")
            sql_command_create += tmp_line

    sql_command_create += "primary key (`id`))"
    # print(sql_command_create)
    print("建立表")
    # print(field_list)
    creat_biao(sql_command_create)

    # 插入数据
    insert_sql = "INSERT INTO `public_data_2`.`{}`(name_first,".format(myname)
    for i in field_list:
        t = i + ','
        insert_sql += t
    insert_sql = insert_sql[0:-1] + ") VALUES ("
    # print(insert_sql)
    print("插入数据")
    for t_i in mylist_all:
        insert_sql1 = insert_sql
        # print(t_i)
        for one in t_i:
            # print(one)
            tmp = "\""+str(one)+"\""+","
            insert_sql1 += tmp
        insert_sql1 = insert_sql1[0:-1]+")"
        # print(insert_sql1.split("VALUES")[1][0:20])
        try:
            insert_data(insert_sql1)
        except:
            print("出错")
        # print()
        # exit()


def travel_data():
    import glob
    myfile_path = glob.glob(r"C:\Users\Administrator\Desktop\1111\all\*.xlsx")
    for i in myfile_path:
        print(i)
        i_name = i.replace(' ', '_')
        i_name = i_name.replace('-', '_')
        # print(i_name)
        myname = i_name.split('\\')[-1].split('.')[0]
        print(myname)
        print()
        read_data_from_pandas(i, myname)


if __name__ == '__main__':
    # read_data_from_pandas()
    # insert_data()
    travel_data()

"""
Create table `public_data`.`finance`(
  `name_first` varchar(30) NOT NULL,
  `province` text,
  `frequency` text,
  `statistic_units` text,
  `first_record` time,
  `last_record` time,
  `pjs` varchar(30),
  `fc` varchar(30),
  `bzc` varchar(30),
  `pd` varchar(30),
  `fd` varchar(30),
  `byxs` varchar(30),
  `max` varchar(30),
  `min` varchar(30),
  `mid` varchar(30),
  `num_record` varchar(30),

  `1947` varchar(30),
  `1948` varchar(30),
  `1949` varchar(30),
  `1950` varchar(30),
  `1951` varchar(30),
  `1952` varchar(30),
  `1953` varchar(30),
  `1954` varchar(30),
  `1955` varchar(30),
  `1956` varchar(30),
  `1957` varchar(30),
  `1958` varchar(30),
  `1959` varchar(30),
  `1960` varchar(30),
  `1961` varchar(30),
  `1962` varchar(30),
  `1963` varchar(30),
  `1964` varchar(30),
  `1965` varchar(30),
  `1966` varchar(30),
  `1967` varchar(30),
  `1968` varchar(30),
  `1969` varchar(30),
  `1970` varchar(30),
  `1971` varchar(30),
  `1972` varchar(30),
  `1973` varchar(30),
  `1974` varchar(30),
  `1975` varchar(30),
  `1976` varchar(30),
  `1977` varchar(30),
  `1978` varchar(30),
  `1979` varchar(30),
  `1980` varchar(30),
  `1981` varchar(30),
  `1982` varchar(30),
  `1983` varchar(30),
  `1984` varchar(30),
  `1985` varchar(30),
  `1986` varchar(30),
  `1987` varchar(30),
  `1988` varchar(30),
  `1989` varchar(30),
  `1990` varchar(30),
  `1991` varchar(30),
  `1992` varchar(30),
  `1993` varchar(30),
  `1994` varchar(30),
  `1995` varchar(30),
  `1996` varchar(30),
  `1997` varchar(30),
  `1998` varchar(30),
  `1999` varchar(30),
  `2000` varchar(30),
  `2001` varchar(30),
  `2002` varchar(30),
  `2003` varchar(30),
  `2004` varchar(30),
  `2005` varchar(30),
  `2006` varchar(30),
  `2007` varchar(30),
  `2008` varchar(30),
  `2009` varchar(30),
  `2010` varchar(30),
  `2011` varchar(30),
  `2012` varchar(30),
  `2013` varchar(30),
  `2014` varchar(30),
  `2015` varchar(30),
  `2016` varchar(30),
  `2017` varchar(30),
  `2018` varchar(30),
  `2019` varchar(30),

  primary key (`name_first`)
)

"""