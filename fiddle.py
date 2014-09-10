from couchbase import Couchbase

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Couchbase')
    parser.add_argument('host', type=str,
                        help='the ip of your couchbase server')
    parser.add_argument('bucket', type=str, default='default', nargs='?',
                        help='name of couchbase bucket')

    args = parser.parse_args()

    return args

def run():

    args = parse_args()

    cb = Couchbase.connect(bucket=args.bucket,  host=args.host)




if __name__ == "__main__":
    run()
