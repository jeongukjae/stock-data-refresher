# -*- coding: utf8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def create(url, echo):
    return create_engine(url, echo=echo, encoding='utf-8')

def session(engine):
    return sessionmaker(bind=engine)()
