import json
from datetime import datetime


def get_operations():
    result = []
    with open('operations.json', 'rt', encoding='utf-8') as data_file:
        for item in json.loads("".join(data_file.readlines())):
            if item:
                result.append(item)
    return result

def filter_by_state(data_list: list, st_val: str) -> list:
    result = []
    for item_dict in data_list:
        if item_dict['state'] == 'EXECUTED':
            result.append(item_dict)
    return result

