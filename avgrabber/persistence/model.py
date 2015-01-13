# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, String, Integer, create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.sql.schema import ForeignKey
from avgrabber.config import PERSISTENCE_SCHEMA

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


Base = declarative_base(cls=BaseMixin)


class Update(Base):
    at = Column(DateTime())
    ads = relationship("Ad", backref='update')


class Ad(Base):
    url = Column(String(255))
    title = Column(String(255))
    placed = Column(DateTime())
    price = Column(Integer())
    update_id = Column(Integer, ForeignKey('update.id'))

engine = create_engine(PERSISTENCE_SCHEMA)
engine.echo = True
Base.metadata.bind = engine
Base.metadata.create_all()
DBSession.configure(bind=engine)


#DBSession().query(Ad).all()
