import time
from business.bR import BusinessRe
from common.yamlLoader import YamlRead

env_config = YamlRead().env_config()
api_config = YamlRead().api_config()


class DataCreate:
    """创建用例前置和后置数据"""
    host = env_config['host']

    def note_create(self, num, user_id, sid, group_id=None, remind_time=None):
        """通用的便签新建方法"""
        note_lists = []
        for i in range(num):
            note_id = str(int(time.time() * 1000))
            # 新建便签主体接口
            url_info = self.host + api_config['note_create_info']['path']

            if remind_time:  # 日历便签
                body = {
                    "noteId": note_id,
                    "remindTime": remind_time,
                    "remindType": 0,
                    'star': 0
                }

            elif group_id:  # 分组便签
                body = {
                    "noteId": note_id,
                    "groupId": group_id,
                    'star': 0
                }

            else:
                body = {
                    "noteId": note_id,
                    'star': 0
                }

            BusinessRe.post(url_info, sid=sid, user_id=user_id, body=body)

            url_content = self.host + api_config['note_create_content']['path']
            body = {
                "noteId": note_id,
                "title": '75u8dlZyTLqWCm/b2PLNlg==',
                "summary": 'pIDnRrCwq8sUW3gyWpo7iw==',
                "body": 'wlby4RxbJjQKcx7rwTpn/w==',
                "localContentVersion": 1,
                "BodyType": 0
            }

            BusinessRe.post(url_content, sid=sid, user_id=user_id, body=body)
            note_lists.append(body)
        return note_lists
