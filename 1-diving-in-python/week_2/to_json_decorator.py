"""
Декоратор to_json

Чтобы передавать данные между функциями, модулями или разными системами
используются форматы данных. Одним из самых популярных форматов является JSON.

Напишите декоратор to_json, который можно применить к различным функциям,
чтобы преобразовывать их возвращаемое значение в JSON-формат.
"""

import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapped
