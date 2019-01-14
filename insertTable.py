from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
from flask import Flask


APP = Flask(__name__)

dynamodb = boto3.resource(
    'dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Movies')


def insert_data_cliente(json_cliente):
    print("json chegou")
    print(json_cliente)
    print("Adding data:")
    table.put_item(
        Item={
            'idfoo': 1,
            'title': 412341234,
        }
    )


def main():
    """Function to good practice"""
    return APP.run()


if __name__ == "__main__":
    main()
