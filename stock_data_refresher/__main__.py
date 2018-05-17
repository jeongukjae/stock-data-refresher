# -*- coding: utf8 -*-
import argparse
import time

# pylint:disable=W0614
from .models import *
# pylint:enable=W0614
from .parser import insert_all, insert_price

def parse_args():
    parser = argparse.ArgumentParser(description='Stock Data Refresher')
    subparsers = parser.add_subparsers(help='functions of stock data refresher', dest='kind')
    subparsers.required = True

    database_subparser = subparsers.add_parser('db', help='managements of databse')
    database_subparser.add_argument('action', type=str, help='things to do', choices=['create', 'truncate', 'drop'])
    database_subparser.add_argument('--uri', type=str, help='database uri.', required=True)
    database_subparser.add_argument('--echo', help='echo log (database)', action="store_true")

    stocks_subparser = subparsers.add_parser('stock', help='functions about stocks')
    stocks_subparser.add_argument('action', type=str, help='things to do', choices=['put_list', 'put_in_loop', 'put_once'])
    stocks_subparser.add_argument('--uri', type=str, help='database uri.', required=True)
    stocks_subparser.add_argument('--echo', help='echo log (database)', action="store_true")
    stocks_subparser.add_argument('--time', help='time of sleeping of each loops. (seconds, 5s as default)', type=int, default=5)

    args = parser.parse_args()

    if args.kind == 'db':
        from .engine import Base, create
        engine = create(args.uri, args.echo)

        if args.action == 'create':
            Base.metadata.create_all(engine)

        elif args.action == 'truncate':
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)

        elif args.action == 'drop':
            Base.metadata.drop_all(engine)
    
    elif args.kind == 'stock':
        from .engine import Base, create, session
        engine = create(args.uri, args.echo)
        sess = session(engine)

        if args.action == 'put_list':
            insert_all(sess)

        elif args.action == 'put_in_loop':
            ti = args.time
            while True:
                insert_price(sess)
                time.sleep(ti)

        elif args.action == 'put_once':
            insert_price(sess)

if __name__ == "__main__":
    parse_args()
