from utils import load_operations, get_new_data, filtered_data

json_file = 'operations.json'


def main():
    """
    получает данные и выводит 5 последних транзакций
    """
    data = load_operations(json_file)
    data = get_new_data(data)

    for i in range(5):
        print(filtered_data(data[i]))


if __name__ == '__main__':
    main()