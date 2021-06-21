# -*-coding:utf-8-*-
# @Time    : 2019/11/8 0008 10:19
# @Author  :zhu
# @File    : test_reques_Rec.py
# @task description :

import json
import requests
import pprint
import time
import warnings
warnings.filterwarnings("ignore")
"""医保的"""
def request_test_YBicd10(tmp_url):
    url = 'http://{}/api/recommend/yibao'.format(tmp_url)
    data = {
            "hosID": "12345678",
            "codeVersion": "GUOJIA_LC_ICD10_2.0",
            "taskList": [
                        {"id": 1, "code": "As01.000", "codeName": "伤寒t"},
                        {"id": 2, "code": "A01.000t", "codeName": "头皮血肿asdas"}
                        ]
            }
    data_json = json.dumps(data)
    r = requests.post(url, data_json)

    result = r.content

    result = json.loads(result)
    pprint.pprint(result)


def request_test_YBicd9(tmp_url):
    t1 = time.time()
    url = 'http://{}/api/recommend/yibao'.format(tmp_url)
    data = {
    "codeVersion":"GUOJIA_LC_ICD9_2.0",
    "taskList": [
                {
                    "code": "",
                    "codeName": "脊柱针刀治疗",
                    "id": 1700000000
                }
                    ]

}
    data_json = json.dumps(data)
    r = requests.post(url, data_json)

    result = r.content
    result = json.loads(result)
    pprint.pprint(result)
    print(u'消耗时间是：', time.time() - t1)
    """
    单进程模式：12条数据，消耗时间是5.671s    
               216条数据，消耗时间是97s
    多进程模式：12条数据，消耗时间是10.34s
               216条数据，消耗时间是35s
    """

"""临床20的"""
def request_test_LCicd10(tmp_url):
    url = 'http://{}/api/recommend/linchuang2'.format(tmp_url)
    data = {
            "hosID": "12345678",
            "codeVersion": "GUOJIA_YB_ICD10_1.0",
        "taskList": [{
            "code": "47.0100",
            "codeName": "口腔肿物",
            "id": 1
        },
            {
                "code": "",
                "codeName": "阑尾术后",
                "id": 2
            }
        ]
            }
    data_json = json.dumps(data)
    r = requests.post(url, data_json)

    result = r.content
    print(result)
    result = json.loads(result)
    pprint.pprint(result)


def request_test_LCicd9(tmp_url):
    url = 'http://{}/api/recommend/linchuang2'.format(tmp_url)
    data = {
            "hosID": "12345678",
            "codeVersion": "GUOJIA_YB_ICD9_CM3_1.0",
            "taskList": [{
                    "code": "1",
                    "codeName": "脊柱针刀治疗",
                    "id": 1
                }
            ]
            }
    data_json = json.dumps(data)
    r = requests.post(url, data_json)

    result = r.content

    result = json.loads(result)
    pprint.pprint(result)



if __name__ == '__main__':

    tmp_url = "10.246.0.4:8014"
    tmp_url = "192.168.2.152:8011"
    # tmp_url = "192.168.2.171:8001"
    request_test_YBicd9(tmp_url)
    # request_test_YBicd10(tmp_url)

    request_test_LCicd9(tmp_url)
    # request_test_LCicd10(tmp_url)
