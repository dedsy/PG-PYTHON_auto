import json


def data_from_json(json_file_name: str):
    """Функция принимает путь к файлу json и возвращает словарь с данными из файла"""
    with open(json_file_name, encoding='utf-8') as f:
        f_data = json.load(f)
    return f_data


def info(data_dict: dict, *args):
    """Функция принимает словарь и список ключей, согласно которым она выводит информацию
    (если ключа нет - напротив него стоит значение "данные отсуствуют") в 2 столбика (ключ  значение)
    - рекомендация использовать f-строки"""
    for el in args:
        if data_dict.get(el):
            print(f"{el:<10}- {data_dict.get(el)}")
        else:
            print(f"{el:<10}- {data_dict.get(el, 'данные отсутствуют')}")


def change_value(json_file_name:str, key: str, value: str):
    """Функция принимает словарь, ключ и новое значение, которое будет присвоено этому ключу,
    если он существует, если нет - выдать сообщение, что такого ключа нет"""
    f_data = data_from_json(json_file_name)
    if key in f_data.keys():
        f_data[key] = value
    else:
        print(f'Ключа {key} не существует')
    with open(json_file_name, 'w', encoding='utf-8') as f:
        json.dump(f_data, f)
