import json


def load_operations(path):
    """
    достает данные из файла с json
    :param path: list
    :return: информацию о операции клиента
    """
    with open(path, 'r', encoding='utf-8') as file:
        operation_data = json.load(file)
        return operation_data


def get_new_data(operation_data):
    """
    отфильтровыет данные по параметру
    :param operation_data: list
    :return: Отфильтрованную информацию о операции клиента
    """
    operation_data = [item for item in operation_data if item.get('state') == 'EXECUTED']
    operation_data = sorted(operation_data, key=lambda item: item['date'], reverse=True)
    return operation_data


def filtered_data(data):
    """
    функция вытаскивает только нужные для показа строки
    :param data: str
    :return: информацию о транзакции
    """
    operation_date = format_data(data.get("date"))

    if data.get('from'):
        card_from = card_number_hide(data.get('from'))
    else:
        card_from = ' '
    count_to = card_number_hide(data.get('to'))

    return f'{operation_date} {data.get("description")}\n' \
           f'{card_from} -> {count_to}\n' \
           f'{data["operationAmount"]["amount"]} {data["operationAmount"]["currency"]["name"]}\n'


def format_data(str_date):
    """
    форматирует дату операции
    :param str_date: str
    :return: дату в формате ДД.ММ.ГГГГ
    """
    operation_date = str_date[:10].split('-')
    return '.'.join(reversed(operation_date))


def card_number_hide(card):
    """
    скрывает номер банковской карты и счета
    :param card: str
    :return: замаскированный номер банковской карты
    """
    card = card.split(' ')
    if card[0] == "Счет":
        return f'{card[0]} **{card[-1][-4:]}'
    return f'{" ".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'
