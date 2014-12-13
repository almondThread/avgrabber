# -*- coding: utf-8 -*-
from utils.data import normalize_data

def print_csv(data_line):
    d = normalize_data(data_line)
    order = ('date', 'title', 'price', 'link', 'id')
    data = [d[x] for x in order]
    print(', '.join(data))