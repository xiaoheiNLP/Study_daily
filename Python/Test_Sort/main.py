# -*-encoding:utf8-*-
import json
from flask import *
from flask_cors import CORS
from retrieval import WhooshIndex, load_dict_icd10_dict, load_dict_icd10_4_df, standard_datebase
from retrieval import load_dict_icd9_dict, load_dict_icd9_4_df
from retrieval import simWord_dict_icd9, simWord_dict_icd10
from sel_10 import matchTermsDict_10
from sel_9 import matchTermsDict_9
from sel import matchTermsDict2
import hashlib
from coding import Coding
from db import *
import warnings
warnings.filterwarnings('ignore')

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
CORS(app, resources=r'/*')

# demo里面验证
md = hashlib.md5()  # 构造一个md5
md.update('admin')

# 初始化
# coding = Coding()
# dict_table = DictTable()
# dict_table.constructureDict10()
# dict_table.constructureDict9()
# dict_table.constructureBlzd()
# dict_table.constructureWbss()

from sel_10_function import LogMgr
logm = LogMgr("log1")


@app.route('/api/v1/terms/login', methods=['GET', 'POST'])
def login1():
    scret_str = md.hexdigest()
    if request.method == "POST":
        data = json.loads(request.get_data())
        # print(icd_file_pkl)
        if (data["username"] == "admin" )&(data["password"] == scret_str):
            return json.dumps({"errCode": 0, "errMsg":""})
        else:
            return json.dumps({"errCode": 1, "errMsg": u"账号或密码错误"})
    else:
        return json.dumps({"errCode": 1, "errMsg": u"账号或密码错误"})


@app.route('/api/v2/terms/login', methods=['GET', 'POST'])
def login2():
    scret_str = md.hexdigest()
    if request.method == "POST":
        data = json.loads(request.get_data())
        # print(icd_file_pkl)
        if (data["username"] == "admin" )&(data["password"] == scret_str):
            return json.dumps({"errCode":0,"errMsg":""})
        else:
            return json.dumps({"errCode": 1, "errMsg": u"账号或密码错误"})
    else:
        return json.dumps({"errCode": 1, "errMsg": u"账号或密码错误"})

# 没有用
@app.route('/api/v1/terms', methods=['GET', 'POST'])
def terms1():
    # 将请求的别名 转化为临床术语，和标准名称
    if request.method == 'POST':
        data = json.loads(request.get_data())

        if data['keyWordType'] == "icd10":
            temp_, total_result_code, total_result_name, temp, temp1 = load_dict_icd10_dict
            index = WhooshIndex(index_path="./icd10_index", total_result_code=total_result_code, total_result_name=total_result_name)
            return json.dumps(index.search(words=data["keyWordStr"]))

        elif data['keyWordType'] == "icd9":
            temp_, total_result_code, total_result_name, temp, temp1 = load_dict_icd9_dict
            index = WhooshIndex(index_path="./icd9_index", total_result_code=total_result_code, total_result_name=total_result_name)
            return json.dumps(index.search(words=data["keyWordStr"]))
            pass
        elif data['keyWordType'] == "blzd":
            # total_result_code, total_result_name = load_dict_blzd()
            # index = WhooshIndex(index_path="", total_result_code=total_result_code, total_result_name=total_result_name)
            # return json.dumps(index.search(words=icd_file_pkl["keyWordStr"]))
            pass
        else:
            pass

    else:
        return "error"


# 没有用
@app.route('/api/v2/terms', methods=['GET', 'POST'])
def terms2():
    # 将请求的别名 转化为临床术语，和标准名称
    if request.method == 'POST':
        data = json.loads(request.get_data())

        logm.info(u"任务类型:{0}, 推荐语句：{1}".format(data["keyWordType"], data["keyWordStr"]))
        print u"任务类型:{0}, 推荐语句：{1}".format(data["keyWordType"], data["keyWordStr"])
        if data['keyWordType'] == "icd10":
            result_dict1 = load_dict_icd10_dict
            select_df = load_dict_icd10_4_df
            # 查询函数
            result = matchTermsDict_10(select_str=data["keyWordStr"], select_df=select_df, standard_datebase=standard_datebase,
                                         result_dict=result_dict1, simWord_dict=simWord_dict_icd10)

            return json.dumps(result)

        elif data['keyWordType'] == "icd9":
            result_dict = load_dict_icd9_dict
            select_df = load_dict_icd9_4_df
            # 查询函数
            result = matchTermsDict_9(select_str=data["keyWordStr"], select_df=select_df, result_dict=result_dict, simWord_dict=simWord_dict_icd9)
            return json.dumps(result)

        elif data['keyWordType'] == "blzd":
            # total_result_code, total_result_name = load_dict_blzd()
            # index = WhooshIndex(index_path="", total_result_code=total_result_code, total_result_name=total_result_name)
            # return json.dumps(index.search(words=icd_file_pkl["keyWordStr"]))
            pass

        else:
            pass

    else:
        return "error"


# 这个是给医生工作站用的，叫临床版
@app.route('/api/v_hospital/coder', methods=['GET', 'POST'])
def terms2_2():
    # 将请求的别名 转化为临床术语，和标准名称
    if request.method == 'POST':
        data = json.loads(request.get_data())
        print data
        if data['keyWordType'] == "icd10":
            result_dict = load_dict_icd10_dict
            # 查询函数
            print "api-v_hospital-%s版本：%s, 搜索关键词为：%s" % (data['keyWordType'],data['codeVersion'], data['keyWordStr'])
            result = matchTermsDict2(select_str=data["keyWordStr"], result_dict=result_dict)

            return json.dumps(result)
        elif data['keyWordType'] == "icd9":
            result_dict = load_dict_icd9_dict
            # 查询函数
            print "api-v_hospital-%s版本：%s, 搜索关键词为：%s" % (data['keyWordType'], data['codeVersion'], data['keyWordStr'])
            result = matchTermsDict2(select_str=data["keyWordStr"], result_dict=result_dict)
            return json.dumps(result)
        elif data['keyWordType'] == "blzd":
            # total_result_code, total_result_name = load_dict_blzd()
            # index = WhooshIndex(index_path="", total_result_code=total_result_code, total_result_name=total_result_name)
            # return json.dumps(index.search(words=icd_file_pkl["keyWordStr"]))
            pass
        else:
            pass

    else:
        return "error"


# 这个是给悦励专业版用的叫：标准版
@app.route('/api/v1/coder', methods=['GET', 'POST'])
def terms3():
    # 将请求的别名 转化为临床术语，和标准名称
    if request.method == 'POST':
        # print request.get_data()
        data = json.loads(request.get_data())
        # icd_file_pkl = coding.urlDecoding(dict(icd_file_pkl))
        # print icd_file_pkl
        if data['keyWordType'] == "icd10":
            # 获取icd版本
            icd_v = data['codeVersion']

            icd_v = dict_table.map_10_dict.get(icd_v,None)
            item = data['keyWordStr']
            print "api-v1-coder-icd10版本：%s, 搜索关键词为：%s" % (icd_v, item)
            # 如果输入的是全字母，首字母匹配，如果是汉字，使用关键字匹配
            if coding.checkAlpha(item):
                result = coding.mathTermsAlphDict(select_str=item,
                                                  result_dict=[dict_table.icd_10_alph_dict[icd_v],dict_table.icd_10_dict[icd_v]])
            else:
                # print item
                result_dict = [dict_table.icd_10_dict[icd_v], dict_table.icd_10_words[icd_v]]
                result = coding.matchTermsDict(item, result_dict=result_dict)
            return json.dumps(result)
        elif data['keyWordType'] == "icd9":
            icd_v = data['codeVersion']
            icd_v = dict_table.map_9_dict.get(icd_v, None)
            item = data['keyWordStr']
            print "api-v1-coder-icd9版本：%s, 搜索关键词为：%s"%(icd_v,item)
            if coding.checkAlpha(item):
                result = coding.mathTermsAlphDict(select_str=item,
                                                  result_dict=[dict_table.icd_9_alph_dict[icd_v],dict_table.icd_9_dict[icd_v]])
            else:
                # print item
                result_dict = [dict_table.icd_9_dict[icd_v], dict_table.icd_9_words[icd_v]]
                result = coding.matchTermsDict(item, result_dict=result_dict)
            return json.dumps(result)
        elif data['keyWordType'] == "blzd":
            # 获取icd版本
            icd_v = data['codeVersion']
            icd_v = dict_table.map_10_dict.get(icd_v, None)
            item = data['keyWordStr']
            print "api-v1-coder-icd10-blzd版本：%s, 搜索关键词为：%s" % (icd_v, item)
            # 如果输入的是全字母，首字母匹配，如果是汉字，使用关键字匹配
            if coding.checkAlpha(item):
                result = coding.mathTermsAlphDict(select_str=item,
                                                  result_dict=[dict_table.icd_blzd_alph_dict[icd_v], dict_table.icd_blzd_dict[icd_v]])
            else:
                result_dict = [dict_table.icd_blzd_dict[icd_v], dict_table.icd_blzd_words[icd_v]]
                result = coding.matchTermsDict(item, result_dict=result_dict)
            return json.dumps(result)

        elif data['keyWordType'] == "wbss":
            # 获取icd版本
            icd_v = data['codeVersion']
            # print icd_v
            icd_v = dict_table.map_10_dict.get(icd_v, None)
            item = data['keyWordStr']
            print "api-v1-coder-icd10版本-wbss：%s, 搜索关键词为：%s" % (icd_v, item)
            # 如果输入的是全字母，首字母匹配，如果是汉字，使用关键字匹配
            if coding.checkAlpha(item):
                result = coding.mathTermsAlphDict(select_str=item,
                                                  result_dict=[dict_table.icd_wbss_alph_dict[icd_v],dict_table.icd_wbss_dict[icd_v]])
            else:
                result_dict = [dict_table.icd_wbss_dict[icd_v], dict_table.icd_wbss_words[icd_v]]
                result = coding.matchTermsDict(item, result_dict=result_dict)
            return json.dumps(result)
        else:
            pass
    else:
        return "error"


if __name__ == '__main__':
    app.run(port=8010, host='192.168.2.152')

    # 192.168.2.152     terms2      /api/v2/terms
    # 0.0.0.0