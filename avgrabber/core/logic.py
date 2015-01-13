# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.sql.functions import func
from sqlalchemy import desc
from avgrabber.persistence.model import DBSession, Ad, Update, Project
from avgrabber import grabber


def new_project(name, query):
    p = Project(name=name, query=query, at=datetime.now())
    DBSession().add(p)
    DBSession().commit()
    return p


def list_projects():
    return DBSession().query(Project).all()


def list_updates(project_name=None):
    if project_name:
        return DBSession().query(Project)\
            .filter(Project.name == project_name).first()
    else:
        return DBSession().query(Project).all()

def update_project(project_name):
    p = DBSession().query(Project)\
        .filter(Project.name == project_name)

    if p:
        data_lines = grabber.search(p.query)
        ads = add_update(data_lines)
        return ads
    else:
        return None


def resolve_state(ad):
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
    ads = []
    for data_line in data_lines:
        ad = Ad.from_dict(data_line)
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

#def get_last_update():
#    return DBSession().query(Update)\
#        .filter(Update.at == func.max(Update.at).select())\
#        .first()


#def make_ad(data_line):
#    ad = Ad()
#    for k, v in data_line.items():
#        setattr(ad, k, v)
#    return ad


#test
#add_update(
#    [{
#    'title': 'abc',
#    'url':  'http://',
#    'price': 0,
#    'placed': datetime.now()
#    }]
#)
