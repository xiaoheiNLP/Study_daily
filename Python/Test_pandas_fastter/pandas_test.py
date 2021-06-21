# -*-coding:utf-8-*-
# @Time    : 2019/11/9 0009 12:51
# @Author  :zhu
# @File    : pandas_test.py
# @task description :
# -*- coding: utf-8 -*-
# @Time    : 12/06/18 15:01
# @Author  : SunGuangYang
# @version    : v0.0.1
import re
import os
import pandas as pd
import sqlite3 as sql
from sqlalchemy import create_engine
# from func_class import func_map_1

"""
医保编码版本代码如下
icd10:支持5个版本的转码 GUOJIA_YB_ICD10_1.0
1.icd10_v5       北京临床版v5.0_诊断代码         BEIJING_ICD10_V5.0
2.icd10_v6       北京临床版v6.0_诊断代码         BEIJING_ICD10_V6.0
3.icd10_gb       国际标准版（国标版）_诊断代码    GUOJIA_BZ_ICD10
4.icd10_wh20       国家临床版2.0_诊断代码        GUOJIA_LC_ICD10_2.0
5.icd10_gds      广东省版_诊断代码               GUANGDONG_ICD10

icd9:支持4个版本的转码  GUOJIA_YB_ICD9_CM3_1.0
1.icd9_gb       ICD9-CM-3_V5.0_手术代码         BEIJING_ICD9_CM3_V5.0
2.icd9_wh20       国家临床版2.0_手术代码         GUOJIA_LC_ICD9_CM3_2.0
3.icd9_gds      广东省版_手术代码                GUANGDONG_ICD9_CM3
4.icd9_v6       北京临床版v6.0_手术代码          BEIJING_ICD9_CM3_V6.0
"""

# from code_Translate.func_class import LogMgr
# log_mgr = LogMgr("yibao.log", logID="log2")

"""读取字典"""
path = os.path.split(os.path.realpath(__file__))[0]
docPath = path.replace("code_Translate", 'DataBase')
conn = sql.connect(docPath + "/icd10_yibao.db")
conn9 = sql.connect(docPath + "/icd9_yibao.db")


"""数据调用的三个函数"""
def genDict(table, engine):
    ICD = pd.read_sql("select * from %s"%table, engine)
    ICD = ICD[ICD['JBDM'].notnull()]
    code = dict(zip(ICD['JBDM_PRE'], ICD['JBDM']))
    word = dict(zip(ICD['ZYZD'], ICD['JBDM']))
    return code, word


def genDict_2(table, engine):
    ICD = pd.read_sql("select * from %s"%table, engine)
    ICD = ICD[ICD['JBDM'].notnull()]
    code = dict(zip(ICD['JBDM'], ICD['ZYZD']))
    return code


def getHosData(tableName="dict_transcode_icd9_icd10", icdType=9, tVersion = str):
    """
    数据调用函数：加载医院数据,只加载版本是医保的数据
    :param tableName:数据库表名
    :param icdType:icd的类型
    :param tVersion:转换的终点版本
    :return::
    """
    username, key, url, database = 'root', '123456', '114.112.34.242', 'dlcms'
    mysql_engine = create_engine('mysql+pymysql://%s:%s@%s:3310/%s?charset=utf8'
                                 % (username, key, url, database))

    icd10_bz = pd.read_sql("select * from {} where icdType = {} and tVersion = \'{}\'".format(tableName, icdType, tVersion), mysql_engine)
    hos_dict = {}

    for tmp_index, tmp_value in icd10_bz.iterrows():
        tmp_hosID = tmp_value["hospitalId"]
        tmp_sCode = tmp_value["sCode"]
        tmp_sName = tmp_value["sName"]
        tmp_sVersion = tmp_value["sVersion"]
        tmp_tCode = tmp_value["tCode"]
        tmp_tName = tmp_value["tName"]
        tmp_tVersion = tmp_value["tVersion"]
        mergeVersion  = tmp_sVersion + "++" + tmp_tVersion
        if tmp_hosID not in hos_dict:
            hos_dict[tmp_hosID] = {mergeVersion: {tmp_sCode: [tmp_tCode, tmp_tName],
                                                  tmp_sName: [tmp_tCode, tmp_tName]
                                                  }}
        else:
            if mergeVersion not in hos_dict[tmp_hosID]:
                hos_dict[tmp_hosID][mergeVersion] = {tmp_sCode: [tmp_tCode, tmp_tName],
                                                      tmp_sName: [tmp_tCode, tmp_tName]
                                                      }
            else:
                hos_dict[tmp_hosID][mergeVersion][tmp_sCode] = [tmp_tCode, tmp_tName]
                hos_dict[tmp_hosID][mergeVersion][tmp_sName] = [tmp_tCode, tmp_tName]
    return hos_dict


def reData(tableName="dict_transcode_icd9_icd10", hosID=str, icdType=int, tVersion=str):
    """
    数据调用函数：重新加载医院数据，被函数reloadData调用
    :param tableName: 数据库表名
    :param hosID: 医院的ID
    :param icdType: icd类型
    :param tVersion: 转码的终点版本
    :return:
    """
    username, key, url, database = 'root', '123456', '114.112.34.242', 'dlcms'
    mysql_engine = create_engine('mysql+pymysql://%s:%s@%s:3310/%s?charset=utf8'
                                 % (username, key, url, database))

    ICD = pd.read_sql("select * from {0} where hospitalId = {1} and icdType = {2} and tVersion = \"{3}\" ".format(tableName, hosID, icdType, tVersion), mysql_engine)
    result_dict = {}
    for tmp_index, tmp_value in ICD.iterrows():
        tmp_sCode = tmp_value["sCode"]
        tmp_sName = tmp_value["sName"]
        tmp_sVersion = tmp_value["sVersion"]
        tmp_tCode = tmp_value["tCode"]
        tmp_tName = tmp_value["tName"]
        tmp_tVersion = tmp_value["tVersion"]
        mergeVersion = tmp_sVersion + "++" + tmp_tVersion
        if mergeVersion not in result_dict:
            result_dict[mergeVersion] = {tmp_sCode: [tmp_tCode, tmp_tName],
                                                 tmp_sName: [tmp_tCode, tmp_tName]
                                                 }
        else:
            result_dict[mergeVersion][tmp_sCode] = [tmp_tCode, tmp_tName]
            result_dict[mergeVersion][tmp_sName] = [tmp_tCode, tmp_tName]

    return result_dict



hos_dict_icd10 = getHosData(icdType=10, tVersion="GUOJIA_YB_ICD10_1.0")

for i in hos_dict_icd10:
    print(i, hos_dict_icd10[i])
    for j in hos_dict_icd10[i]:
        print(j, hos_dict_icd10[i][j])
    print()
