import json


def get_operations():
    result = []
    with open('operations.json', 'rt', encoding='utf-8') as data_file:
        for item in json.loads("".join(data_file.readlines())):
            if item:
                result.append(item)
    return result

