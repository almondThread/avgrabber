# -*- coding: utf-8 -*-
from .grabber import core as grabber
from .handler.core import add_update

def search(strs):
    data_lines = grabber.search(strs)
    ads = add_update(data_lines)
    lines = []
    for ad in ads:
        lines.append(ad.to_dict())
    return lines

