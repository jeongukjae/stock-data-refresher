# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..engine import Base

class PriceOfStock(Base):
    __tablename__ = 'price_of_stock'
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    price = Column(Integer)
    gap = Column(Integer) # 전일비
    percentage = Column(Float) # 전일비 퍼센트

    stock = relationship('Stock', back_populates='price')

    def __init__(self, price, gap, percentage):
        self.price = price
        self.gap = gap
        self.percentage = percentage
