"""
Key-value хранилище

Утилита может вызваться со следующими параметрами:
--key <имя ключа> , где <имя ключа> - ключ по которому получаются значения.
Записать в хранилище значения по ключу:
--key <имя ключа> --val <значение>, где <значение> - сохраняемое значение.
"""

import os
import tempfile
import argparse
import json


def get_storage_data():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.exists(storage_path):
        with open(storage_path, 'r', encoding='utf8') as f:
            json_data = json.load(f)
            return json_data


def set_storage_data(data_to_put):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w', encoding='utf8') as f:
        json.dump(data_to_put, f)


def add_value(k, v):
    data = get_storage_data() or dict()
    if k in data:
        data[k] += ', ' + v
    else:
        data[k] = v
    set_storage_data(data)


def get_value(k):
    data = get_storage_data()
    if data is not None and k in data:
        print(data[k], sep=', ')
        return data[k]
    else:
        print(None)
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-key', '--key')
    parser.add_argument('-value', '--value')
    args = parser.parse_args()
    key = args.key
    val = args.value
    if key and val:
        add_value(key, val)
    elif key:
        get_value(key)
