import unittest
from common.caseOutput import error


class AssertCommon(unittest.TestCase):
    def code_assert(self, expect, actual):
        if expect != actual:
            text = f'res code different, expect code: {expect}, actual code: {actual}.'
            error('assert fail! ' + text)
            self.fail(text)

    def __assertEqual(self):
        pass

    def json_assert(self, expect, actual):
        """
        json通用断言方法
        :param expect: 定义预期返回体
        :param actual: 实际返回的json
        :return: 断言成功返回None，断言失败触发fail
        """
        # 字段是否存在的校验
        for key, value in expect.items():
            self.assertIn(key, actual.keys())
        # 校验是否存在多余的字段
        self.assertEqual(len(expect.keys()), len(actual.keys()),
                         msg=f'response keys len different, response keys have: {list(actual.keys())}')
        for key, value in expect.items():
            # 进行数据类型的校验
            if isinstance(value, type):
                self.assertEqual(value, type(actual[key]),
                                 msg=f'{key} type error! actual type is {str(type(actual[key]))}')
            elif isinstance(value, list):
                for i in range(len(value)):
                    if isinstance(value[i], type):
                        self.assertEqual(value[i], type(actual[key][i]),
                                         msg=f'list element {actual[key][i]} type different, actual response {actual[key]}')
                    elif isinstance(value[i], dict):
                        self.json_assert(value[i], actual[key][i])
                    else:
                        self.assertEqual(value[i], actual[key][i],
                                         msg=f'list element {actual[key][i]} value different, actual response {actual[key]}')
            else:
                self.assertEqual(value, actual[key],
                                 msg=f'{key} value error! actual value is {str(actual[key])}')
