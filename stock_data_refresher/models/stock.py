# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey

from ..engine import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    code = Column(String(8))
