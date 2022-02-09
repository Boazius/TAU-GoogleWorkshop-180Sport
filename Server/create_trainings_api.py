import json
import requests


def create_closest_training_for_each_group():
    url = 'http://127.0.0.1:5000/admin/get_all_groups_sp/'
    headers = {
        'secret-code': 'G6kdi6pN0AFxo01x',
        'Content-Type': 'application/json'
    }
    headers1 = {
        'secret-code': 'G6kdi6pN0AFxo01x',
    }
    groups_from_db = requests.get(url, headers=headers1).json()['list of group']
    print(groups_from_db)
    for group in groups_from_db:
        url2 = 'http://127.0.0.1:5000/training/by_group_id_sp/'
        payload = json.dumps({
            "group_id": int(group['id'])
        })
        response = requests.post(url2, headers=headers, data=payload)
        print(response.json())


create_closest_training_for_each_group()
