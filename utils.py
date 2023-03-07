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

def templ_operation(oper_dict: dict):
    data_op = format_date(oper_dict['date'])
    descr_op = oper_dict['description']
    source_op = oper_dict.get('from') if oper_dict.get('from') else ''
    destin_op = oper_dict['to']
    amount_op = oper_dict['operationAmount']['amount']
    currency_op = oper_dict['operationAmount']['currency']['name']
    return data_op, descr_op, source_op, destin_op, amount_op, currency_op

def format_date(date: str):
    date_type = datetime.strptime(date[:10], "%Y-%m-%d")
    result = date_type.strftime("%d.%m.%Y")
    return result