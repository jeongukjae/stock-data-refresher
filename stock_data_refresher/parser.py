# -*- coding: utf8 -*-
# from http://finance.daum.net/xml/xmlallpanel.daum?stype=P&type=U

import re

import requests

def get(url):
    response = requests.get(url)

    result = re.split(r"upjong :", response.text)

    categories = []
    stocks = []

    for data in result[1:]:
        category = re.findall(r'{name : "(.+)",code:"(.+)",avg:"(.+)"}', data)[0]
        categories.append(category)

        stock = re.findall(r'{code:"(.+)",name :"(.+)",cost :"(.+)",updn :"(.+)",rate :"(.+)"}', data)
        stocks.extend(stock)

    return category, stocks

def get_kosdaq():
    return get('http://finance.daum.net/xml/xmlallpanel.daum?stype=Q&type=U')

def get_kospi():
    return get('http://finance.daum.net/xml/xmlallpanel.daum?stype=P&type=U')
