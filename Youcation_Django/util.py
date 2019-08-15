import json


def get_server_info_value(key: str):
    with open('setting_info.json', mode='rt', encoding='utf-8') as file:
        data = json.load(file)

        for k, v in data.items():
            if k == key:
                return v
        raise ValueError('서버 설정을 불러올 수 없습니다.')