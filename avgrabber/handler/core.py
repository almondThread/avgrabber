# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.sql.functions import func
from sqlalchemy import desc
from avgrabber.persistence.model import DBSession, Ad, Update


def get_last_update():
    return DBSession().query(Update)\
        .filter(Update.at == func.max(Update.at).select())\
        .first()


def make_ad(data_line):
    ad = Ad()
    for k, v in data_line.items():
        setattr(ad, k, v)
    return ad


def resolve_state(ad):
#def resolve_state(ad, last_update):

    state = 'new'

    prev_ad = DBSession.query(Ad).join(Update)\
        .filter(Ad.id == ad.id)\
        .order_by(desc(Update.at))\
        .first()
    if not prev_ad:
        state = 'new'
    elif prev_ad.price != ad.price:
        state = 'changed'
    else:
        state = 'unchanged'

    return state


def add_update(data_lines):
    #last_update = get_last_update()

    ads = []
    for data_line in data_lines:
        ad = make_ad(data_line)
        ad.state = resolve_state(ad)
        if ad.state in ['new', 'changed']:
            ads.append(ad)

    update = Update(at=datetime.now())
    DBSession().add(update)
    for ad in ads:
        ad.update = update
    DBSession().add_all(ads)
    DBSession().commit()

    return ads

def get_update_data(update):
    pass

#test
#add_update(
#    [{
#    'title': 'abc',
#    'url':  'http://',
#    'price': 0,
#    'placed': datetime.now()
#    }]
#)
