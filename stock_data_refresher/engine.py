# -*- coding: utf8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create(url, echo):
    return create_engine(url, echo=echo)
