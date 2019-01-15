from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
from flask import Flask
from getAllTable import DecimalEncoder
from operator import itemgetter

APP = Flask(__name__)

dynamodb = boto3.resource(
    'dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
print("colocando o endpoint do dynamo")


table = dynamodb.Table('Movies')
print("linkando a table movies")


def insert_table():

    response = DecimalEncoder()
    print("response do getall")
    print(response)
    data = json.loads("whatever")
    latest_goal = max(data["response"], key=itemgetter("idfoo"))
    print("latest_goal teste")
    print(latest_goal)
    #print("json chegou")
    # print(json_cliente)
    #print("Adding data:")
    # table.put_item(
    #    Item={
    #        'idfoo': 2,
    #        'title': 41231231541234,
    #    }
    # )
    print("insertdata cliente")


def main():
    """Function to good practice"""
    print("def main")
    return APP.run()


if __name__ == "__main__":
    print("antes de exe a insert table")
    insert_table()
    print("depois de exe a insert table")
    main()
