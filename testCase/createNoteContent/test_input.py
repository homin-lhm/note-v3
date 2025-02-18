import time
import unittest
import requests
from parameterized import parameterized
from common.assertCommon import AssertCommon
from common.caseOutput import class_case_decoration
from copy import deepcopy
from common.yamlLoader import YamlRead
from business.bR import BusinessRe


@class_case_decoration
class CreateNoteInfo(unittest.TestCase):
    ac = AssertCommon()
    br = BusinessRe()
    env_config = YamlRead().env_config()
    api_config = YamlRead().api_config()['note_create_info']
    host = env_config['host']
    user_id = env_config['user_id']
    wps_sid = env_config['wps_sid']
    path = api_config['path']
    not_must_keys = api_config['notMustKeys']
    must_keys = api_config['mustKeys']
    url = host + path

    def setUp(self) -> None:
        """实现数据清理方法"""
        # step1：获取测试账号下所有便签数据（依赖获取首页便签接口）
        # step2：删除这些便签（依赖删除接口）
        # step3：回收站清空
        pass

    def testCase01_major(self):
        """新增便签主体，主流程"""
        note_id = str(int(time.time()))
        body = {
            "noteId": note_id,
            "star": 0,
            "remindTime": 0,
            "remindType": 0,
            'groupId': None
        }
        res = self.br.post(self.url, self.wps_sid, self.user_id, body)
        self.assertEqual(200, res.status_code)
        expect = {
            'responseTime': int,
            'infoVersion': 1,
            'infoUpdateTime': int
        }
        self.ac.json_assert(expect, res.json())

    def testCase01_must_key(self):
        """新增便签主体，noteId必填项校验，字段缺失"""
        body = {
            "noteId": '',
            "star": 0,
            "remindTime": 0,
            "remindType": 0,
            'groupId': None
        }
        body.pop('noteId')
        res = self.br.post(self.url, self.wps_sid, self.user_id, body)
        self.assertEqual(400, res.status_code)

    def testCase02_must_key(self):
        """新增便签主体，noteId必填项校验，为空字符串"""
        body = {
            "noteId": '',
            "star": 0,
            "remindTime": 0,
            "remindType": 0,
            'groupId': None
        }
        res = self.br.post(self.url, self.wps_sid, self.user_id, body)
        self.assertEqual(400, res.status_code)

    def testCase03_must_key(self):
        """新增便签主体，noteId必填项校验，为None"""
        body = {
            "noteId": None,
            "star": 0,
            "remindTime": 0,
            "remindType": 0,
            'groupId': None
        }
        res = self.br.post(self.url, self.wps_sid, self.user_id, body)
        self.assertEqual(400, res.status_code)

    @parameterized.expand(not_must_keys)
    def testCase04_must_key(self, key):
        """新增便签主体，非必填字段校验，字段缺失"""
        note_id = str(int(time.time()))
        body = {
            "noteId": note_id,
            "star": 0,
            "remindTime": 0,
            "remindType": 0,
            'groupId': None
        }
        body.pop(key)
        res = self.br.post(self.url, self.wps_sid, self.user_id, body)
        self.assertEqual(200, res.status_code)
