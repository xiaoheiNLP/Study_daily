# -*-coding:utf-8-*-
# @Time    : 2019/8/19 0019 11:11
# @Author   :zhuxinquan
# @File    : Post_dict.py
"""

post访问服务
"""
import requests
import json
import pandas as pd

def get_result(inputStr):
    # url = 'http://192.168.2.152:8009/api/v2/terms'    # http://192.168.2.152:8009/
    url = 'http://192.168.2.152:8009/api/v2/terms'
    data = {
        "keyWordStr": inputStr,
        "keyWordType": "icd10"
    }
    data_json = json.dumps(data)
    r = requests.post(url, data_json)

    result = r.content
    result = json.loads(result)
    resList = result["resList"]
    # print resList
    result_list_name = []
    result_list_code = []
    result_list_name_select = []
    result_list_score = []
    for i in resList:
        # print i["nameKey"], i["codeKey"]      # name_select   score
        result_list_name.append(i["nameKey"])
        result_list_code.append(i["codeKey"])
        result_list_name_select.append(i["name_select"])
        result_list_score.append(i["score"])
    result_dict = {"nameKey": result_list_name, "codeKey": result_list_code, "name_select": result_list_name_select, "score":result_list_score}
    print result_dict
    print
    return pd.DataFrame(result_dict)
    # return result_list_name, result_list_name_select, result_list_code, result_list_score


def get_result_1(inputStr, icd_kind):
    # url = 'http://192.168.2.152:8009/api/v2/terms'    # http://192.168.2.152:8009/
    url = 'http://192.168.2.152:8009/api/v2/terms'
    data = {
        "keyWordStr": inputStr,
        "keyWordType": "icd{}".format(icd_kind)
    }
    data_json = json.dumps(data)
    r = requests.post(url, data_json)

    result = r.content

    result = json.loads(result)
    resList = result["resList"]
    result_list_name = []
    result_list_code = []
    result_list_name_select = []
    result_list_score = []
    for i in resList:
        result_list_name.append(i["nameKey"])
        result_list_code.append(i["codeKey"])
        result_list_name_select.append(i["name_select"])
        result_list_score.append(i["score"])
    return result_list_name, result_list_name_select, result_list_code, result_list_score


# 测试老的新的算法有什么不同
def test_oldNew(inputStr):
    url = 'http://192.168.2.172:8009/api/v2/terms'
    data = {
        "keyWordStr": inputStr,
        "keyWordType": "icd10"
    }
    data_json = json.dumps(data)
    r = requests.post(url, data_json)

    result = r.content
    result = json.loads(result)
    resList_1 = result["resList"]

    url = 'http://192.168.2.152:8010/api/v2/terms'
    data = {
        "keyWordStr": inputStr,
        "keyWordType": "icd10"
    }
    data_json = json.dumps(data)
    r = requests.post(url, data_json)

    result = r.content
    result = json.loads(result)
    resList_2 = result["resList"]

    for i1, i2 in zip(resList_1, resList_2):
        print i1
        print i2
        print



if __name__ == '__main__':
    t = [u"高血", u"高血压", u"高血压1", u"冠心病", u"肱骨骨折", u"肱骨远端骨折", u"血友病", u"肱骨近端骨折", u"单侧肱骨骨折",u"A血友病",u"血A友病",u"痔伴",u"痔不伴"]
    t1 = [u"右侧肱骨骨折", u"左侧肱骨骨折", u"双侧肱骨骨折", u"右肱骨干粉碎性骨折", u"痔伴", u"糖尿病型高血压", u"糖尿病"]
    t2 = [u"肾萎缩", u"单侧肾萎缩", u"上肢骨折", u"糖尿病", u"不伴高血压", u"肾萎缩伴高血压", u"肾萎缩不伴高血压" ,u"左" ,u"右" ,u"单", u"双", u"伴", u"不伴"]
    t.extend(t1)
    t.extend(t2)
    print len(t)
    # mydata = pd.read_excel(u'C:/Users/Administrator/Desktop/任务/搜索/手术词.xlsx')
    # t = mydata["zyzd"]
    for i in t:
        print i
        # result = get_result(i)
        # result.to_excel(u"./data/{}.xlsx".format(i))
        test_oldNew(i)
        print

