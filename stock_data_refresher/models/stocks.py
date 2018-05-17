# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from ..engine import Base

class Stocks(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    code = Column(String(8), unique=True)
    market = Column(Enum('Q', 'P')) # P: KOSPI, Q: KOSDAQ

    categories = relationship('CategoryOfStocks', back_populates='stocks')
    price = relationship('PriceOfStock', back_populates='stock', uselist=False)

    def __init__(self, name=None, code=None, market='P'):
        self.name = name
        self.code = code
        self.market = market
