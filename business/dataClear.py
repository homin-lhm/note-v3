from business.bR import BusinessRe
from common.yamlLoader import YamlRead

env_config = YamlRead().env_config()
api_config = YamlRead().api_config()


def all_notes_clear(user_id, sid):
    """指定某一个用户进行全量的便签清理"""
    # 获取全量的便签数据
    host = env_config['host']
    url = host + f'/v3/notesvr/user/{user_id}/home/startindex/0/rows/999/notes'
    res = BusinessRe().get(url, sid)
    for note in res.json()['webNotes']:
        note_id = note['noteId']
        del_url = host + api_config['note_delete']['path']
        body = {'noteId': note_id}
        BusinessRe().post(del_url, user_id=user_id, sid=sid, body=body)
    clean_note_url = host + api_config['cleanRecyclebin']['path']
    body = {
        'noteIds': [-1]
    }
    BusinessRe().post(clean_note_url, user_id=user_id, sid=sid, body=body)


if __name__ == '__main__':
    all_notes_clear(env_config['user_id'], env_config['wps_sid'])
