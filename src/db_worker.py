from typing import Dict

from pymongo import MongoClient
from pymongo.results import InsertOneResult


def get_client(host: str, port: int, **kwargs):
    raise NotImplementedError


def insert_one(
    client: MongoClient,
    document: Dict,
    db_name="test_db",
    collection_name="test_collection",
) -> InsertOneResult:
    raise NotImplementedError


def find_one(
    client: MongoClient,
    document: Dict,
    db_name="test_db",
    collection_name="test_collection",
):
    raise NotImplementedError
