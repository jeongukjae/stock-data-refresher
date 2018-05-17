# -*- coding: utf8 -*-
# from http://finance.daum.net/xml/xmlallpanel.daum?stype=P&type=U

import re

import requests

from .models import Stock, Category, CategoryOfStocks, PriceOfStock
from .time_elapsed import time_elapsed

def get(url):
    print('trying to get stock data from the daum finance...')
    response = requests.get(url)

    result = re.split(r"upjong :", response.text.replace('&nbsp;', '').replace('▲', '+').replace('▼', '-').replace('↓', '-'))

    categories = list()
    stocks = dict()

    for data in result[1:]:
        category = re.findall(r'{name : "(.+)",code:"(.+)",avg:"(.+)"}', data)[0]
        categories.append(category)

        stocks_in_data = re.findall(r'{code:"(.+)",name :"(.+)",cost :"(.+)",updn :"(.+)",rate :"(.+)"}', data)
        for stock in stocks_in_data:
            if stock[0] in stocks:
                stocks[stock[0]]['category'].append(category[1])
            else:
                stocks[stock[0]] = {
                    'code': stock[0],
                    'name': stock[1],
                    'price': stock[2].replace(',', ''),
                    'updn': stock[3].replace(',', ''),
                    'rate': stock[4],
                    'category': [category[1]]
                }

    return categories, stocks

def get_kosdaq():
    return get('http://finance.daum.net/xml/xmlallpanel.daum?stype=Q&type=U')

def get_kospi():
    return get('http://finance.daum.net/xml/xmlallpanel.daum?stype=P&type=U')

def insert(data, session, type):
    categories, stocks = data()

    print('insert data into the database...')
    categories_data = dict()
    for category in categories:
        cat = Category(category[0], category[1], type)
        categories_data[category[1]] = cat
        session.add(cat)

    for _, value in stocks.items():
        print('insert {} (code: {}).'.format(value['name'], value['code']))
        stock = Stock(value['name'], value['code'], type)
        session.add(stock)
        for category in value['category']:
            cos = CategoryOfStocks(value['code'], category)
            stock.categories.append(cos)
            categories_data[category].stocks.append(cos)
        
        price = PriceOfStock(int(value['price']), int(value['updn']), float(value['rate'][:-1]))
        stock.price = price

def insert_only_price(data, session, type, stocks):
    _, crawled_stocks = data()

    print('insert pricing data into the database...')
    for stock in stocks:
        if stock.pq == type:
            print('update {} (code: {}).'.format(stock.name, stock.code))
            value = crawled_stocks[stock.code]

            stock.price.price = int(value['price'])
            stock.price.gap = int(value['updn'])
            stock.price.percentage = float(value['rate'][:-1])

def insert_all(session):
    insert(get_kospi, session, 'P')
    insert(get_kosdaq, session, 'Q')

    print('commit data')
    session.commit()

@time_elapsed
def insert_price(session):
    stocks = session.query(Stock).all()

    insert_only_price(get_kospi, session, 'P', stocks)
    insert_only_price(get_kosdaq, session, 'Q', stocks)

    print('commit data')
    session.commit()
