# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from ..engine import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    code = Column(String(8), unique=True)
    pq = Column(Enum('Q', 'P'))

    categories = relationship('CategoryOfStocks', back_populates='stocks')
    price = relationship('PriceOfStock', back_populates='stock', uselist=False)

    def __init__(self, name=None, code=None, pq='P'):
        self.name = name
        self.code = code
        self.pq = pq
