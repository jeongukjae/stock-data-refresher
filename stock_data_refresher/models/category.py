# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from ..engine import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    code = Column(String(4))
    pq = Column(Enum('Q', 'P'))

    stocks = relationship('CategoryOfStocks', back_populates='categories')

    def __init__(self, name=None, code=None, pq='P'):
        self.name = name
        self.code = code
        self.pq = pq
