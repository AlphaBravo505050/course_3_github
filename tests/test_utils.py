from utils import load_operations, get_new_data, filtered_data, format_data, card_number_hide

def test_load_operations():
    """
    тест функции прочтения json
    :return:
    """
    test_list = [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    assert load_operations('test.json') == test_list


def test_get_new_data():
    """
    тест функции фильтрации по параметру
    :return:
    """
    list_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        }

    ]
    sorted_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",

        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",

        }
    ]

    assert get_new_data(list_data) == sorted_data

def test_format_data():
    """
    тест функции изменения формата даты транзакции
    :return:
    """
    assert format_data('2018-01-26T15:40:13.413061') == '26.01.2018'
    assert format_data('2019-09-11T17:30:34.445824') == '11.09.2019'

def test_card_number_hide():
    """
    Тест функции маскировки номера банковской карты
    :return:
    """
    assert card_number_hide('Visa Platinum 2256483756542539') == 'Visa Platinum 2256 48** **** 2539'
    assert card_number_hide('Счет 73654108430135874305') == 'Счет **4305'
    assert card_number_hide('MasterCard 4956649687637418') == 'MasterCard 4956 64** **** 7418'

def test_filtred_data():
    """
    тест функции показа информации о транзакции по полям
    :return:
    """
    test_dict = {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {
                "amount": "79428.73",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061"
    }
    dict_result = '23.11.2018 Перевод с карты на карту\n' \
                  'Visa Platinum 5355 13** **** 8236 -> Maestro 8045 76** **** 9061\n' \
                  '79428.73 USD\n'

    assert filtered_data(test_dict) == dict_result