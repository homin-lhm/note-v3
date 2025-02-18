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
class GetHomePageInput(unittest.TestCase):
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

    def testCase01_must_key(self):
        """获取当前用户的首页便签，user_id必填项为空字符"""
        info('【前置步骤】请求新增便签主体和新增便签内容接口，构建一条便签数据')
        note_datas = DataCreate().note_create(1, self.user_id, self.wps_sid)

        # 用例操作步骤
        info('【step】获取当前用户的首页便签数据')
        url = self.host + f'/v3/notesvr/user//home/startindex/0/rows/1/notes'
        res = self.br.get(url, self.wps_sid)
        self.ac.code_assert(404, res.status_code)

    def testCase02_must_key(self):
        """获取当前用户的首页便签，user_id必填项为null"""
        info('【前置步骤】请求新增便签主体和新增便签内容接口，构建一条便签数据')
        note_datas = DataCreate().note_create(1, self.user_id, self.wps_sid)

        # 用例操作步骤
        info('【step】获取当前用户的首页便签数据')
        url = self.host + f'/v3/notesvr/user/null/home/startindex/0/rows/1/notes'
        res = self.br.get(url, self.wps_sid)
        self.ac.code_assert(403, res.status_code)
