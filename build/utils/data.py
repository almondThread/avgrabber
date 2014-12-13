# -*- coding: utf-8 -*-
from datetime import date, timedelta

def normalize_string(str):
   return str.replace('\n', "").strip()

def prepare_datetime(dt):
    months = {
        'янв.': 1, 'фев.': 2, 'мар.': 3,
        'апр.': 4, 'мая': 5, 'июн.': 6,
        'июл.': 7, 'авг.': 8, 'сен.': 9,
        'окт.': 10, 'нояб.': 11, 'дек.': 12
    }

    dt = normalize_string(dt).encode('utf-8')
    date_parts = dt.split(" ")

    today = date.today()
    if date_parts[0] == 'Сегодня':
        d = today
    elif date_parts[0] == 'Вчера':
        d = today - timedelta(days=1)
    else:
        day = int(date_parts[0])
        month = int(months[date_parts[1]])
        d = date(today.year, month, day)
        if d > today:
            d -= timedelta(years=1)

    return " ".join([d.strftime('%d.%m.%Y'), date_parts[-1]])

def normalize_data(data_line):
    normalized = {}
    for key in list(data_line.keys()):
        try:
            normalized[key] = normalize_string(data_line[key]).replace(',', "")
        except:
            pass
    return normalized