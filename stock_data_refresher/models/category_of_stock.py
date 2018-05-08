# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..engine import Base

class CategoryOfStocks(Base):
    __tablename__ = 'category_of_stocks'
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    stocks = relationship('Stock', backref='category')
    categories = relationship('Category', backref='stock')
