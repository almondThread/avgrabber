# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, String, Integer, PickleType, create_engine, inspect, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.sql.schema import ForeignKey
from avgrabber.config import config

DBSession = scoped_session(sessionmaker())
class BaseMixin(object):
    query = DBSession.query_property()
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __str__(self):
        return self.__dict__.__str__()

    def to_dict(self):
        mapper = inspect(self)
        dict = {}
        for column in mapper.attrs:
            dict[column.key] = column.value
        return dict

    @staticmethod
    def from_dict(dict):
        ad = Ad()
        for k, v in dict.items():
            setattr(ad, k, v)
        return ad


Base = declarative_base(cls=BaseMixin)


class Project(Base):
    at = Column(DateTime())
    name = Column(String(255), unique=True)
    query = Column(String(500))   # list of strings
    updates = relationship("Update", backref='project')

class Update(Base):
    at = Column(DateTime())
    ads = relationship("Ad", backref='update')
    project_id = Column(Integer, ForeignKey('project.id'))

class Ad(Base):
    url = Column(String(255))
    title = Column(String(255))
    placed = Column(DateTime())
    price = Column(Integer())
    update_id = Column(Integer, ForeignKey('update.id'))

engine = create_engine(config.get('PERSISTENCE_SCHEMA'))
engine.echo = False
Base.metadata.bind = engine
Base.metadata.create_all()
DBSession.configure(bind=engine)


#DBSession().query(Ad).all()
