# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String

from ..engine import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(8))
    code = Column(String(4))
