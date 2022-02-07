import json
import requests


def create_closest_training_for_each_group():
    url = 'https://server-idhusddnia-ew.a.run.app/admin/get_all_groups_sp/'
    headers = {
        'secret-code': 'G6kdi6pN0AFxo01x'
    }
    groups_from_db = requests.get(url, headers=headers).json()['list of group']
    print(groups_from_db)
    for group in groups_from_db:
        url2 = 'https://server-idhusddnia-ew.a.run.app/training/by_group_id_sp/'
        payload = json.dumps({
            "group_id": int(group['id'])
        })
        response = requests.post(url2, headers=headers, data=payload)
        print(response.json())


create_closest_training_for_each_group()
