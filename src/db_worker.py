from typing import Dict, List

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.results import InsertOneResult, InsertManyResult

connections = []


def get_client(host: str, port: int, **kwargs):
    for conn in connections:
        if conn['host'] == host and conn['port'] == port:
            return conn['client']
    connections.append(
        {
            'client': MongoClient(host, port, **kwargs),
            'host': host,
            'port': port
        }
    )
    return connections[-1]['client']


def insert_one(
        client: MongoClient,
        document: Dict,
        db_name="test_db",
        collection_name="test_collection",
) -> InsertOneResult:
    collection = client[db_name][collection_name]
    return collection.insert_one(document)


def insert_many(
        client: MongoClient,
        documents: List[Dict],
        db_name="test_db",
        collection_name="test_collection",
) -> InsertManyResult:
    collection = client[db_name][collection_name]
    return collection.insert_many(documents)


def find_one(
        client: MongoClient,
        document: Dict,
        db_name="test_db",
        collection_name="test_collection",
):
    collection = client[db_name][collection_name]
    return collection.find_one(document)


def find_many(
        client: MongoClient,
        condition: Dict,
        db_name="test_db",
        collection_name="test_collection",
) -> Cursor:
    collection = client[db_name][collection_name]
    return collection.find(condition)


def set_new_value(
        client: MongoClient,
        contidion,
        field,
        new_value,
        create_new: bool = False,
        db_name="test_db",
        collection_name="test_collection",
) -> InsertOneResult:
    collection = client[db_name][collection_name]
    obj = collection.find_one(contidion)
    if obj is not None:
        return collection.update_one(contidion, {
            '$set': {
                field: new_value
            }
        })
    if obj is None and create_new:
        return collection.insert_one({field: new_value})
