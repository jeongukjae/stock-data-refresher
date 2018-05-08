# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..engine import Base

class CategoryOfStocks(Base):
    __tablename__ = 'category_of_stocks'
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    stocks = relationship('Stock', back_populates='categories')
    categories = relationship('Category', back_populates='stocks')
    
    def __init__(self, stock_id=None, category_id=None):
        self.stock_id = stock_id
        self.category_id = category_id
