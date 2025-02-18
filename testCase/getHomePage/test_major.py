import time
import unittest
import requests
from common.assertCommon import AssertCommon
from business.dataClear import all_notes_clear
from business.dataCreate import DataCreate
from common.caseOutput import info, class_case_decoration
from copy import deepcopy
from common.yamlLoader import YamlRead
from business.bR import BusinessRe


@class_case_decoration
class GetHomePageMajor(unittest.TestCase):
    ac = AssertCommon()
    dc = DataCreate()
    br = BusinessRe()
    env_config = YamlRead().env_config()
    host = env_config['host']
    user_id = env_config['user_id']
    wps_sid = env_config['wps_sid']

    def setUp(self) -> None:
        """实现数据清理方法"""
        all_notes_clear(user_id=self.user_id, sid=self.wps_sid)

    def testCase01_major(self):
        """获取当前用户的首页便签，正向流程"""
        info('【前置步骤】请求新增便签主体和新增便签内容接口，构建一条便签数据')
        note_datas = DataCreate().note_create(1, self.user_id, self.wps_sid)

        # 用例操作步骤
        info('【step】获取当前用户的首页便签数据')
        url = self.host + f'/v3/notesvr/user/{self.user_id}/home/startindex/0/rows/1/notes'
        res = self.br.get(url, self.wps_sid)
        expect = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": note_datas[0]['noteId'],
                    "createTime": int,
                    "star": 0,
                    "remindTime": 0,
                    "remindType": 0,
                    "infoVersion": 1,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": note_datas[0]['title'],
                    "summary": note_datas[0]['summary'],
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }
            ]
        }
        self.ac.code_assert(200, res.status_code)
        self.ac.json_assert(expect=expect, actual=res.json())
