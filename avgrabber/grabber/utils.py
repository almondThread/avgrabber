# -*- coding: utf-8 -*-
from datetime import date, timedelta
from dateutils import relativedelta

def normalize_string(str):
   return str.replace('\n', "").strip()

def prepare_datetime(dt):
    months = {
        'янв.': 1, 'фев.': 2, 'мар.': 3,
        'апр.': 4, 'мая': 5, 'июн.': 6,
        'июл.': 7, 'авг.': 8, 'сен.': 9,
        'окт.': 10, 'нояб.': 11, 'дек.': 12
    }

    dt = normalize_string(dt)
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
            d -= relativedelta(years=1)

    return d
    #return " ".join([d.strftime('%d.%m.%Y'), date_parts[-1]])

def prepare_price(price):
    price = normalize_string(price)
    price = price.split(" ")[0]  # remove currency
    price = price.replace("\u00A0", "")  # remove &nbsp symbol
    try:
        price = int(price)
    except ValueError:
        price = 0
    return price

def normalize_data(data_line):
    normalized = {}
    for key in list(data_line.keys()):
        value = data_line[key]
        if isinstance(value, str):
            try:
                normalized[key] = normalize_string(value).replace(',', "")
            except:
                normalized[key] = ""
        else:
            normalized[key] = value
    return normalized