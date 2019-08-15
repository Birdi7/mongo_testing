from typing import Dict, List

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.results import InsertOneResult, InsertManyResult


def get_client(host: str, port: int, **kwargs):
    raise NotImplementedError


def insert_one(
    client: MongoClient,
    document: Dict,
    db_name="test_db",
    collection_name="test_collection",
) -> InsertOneResult:
    raise NotImplementedError


def insert_many(
    client: MongoClient,
    documents: List[Dict],
    db_name="test_db",
    collection_name="test_collection",
) -> InsertManyResult:
    raise NotImplementedError


def find_one(
    client: MongoClient,
    document: Dict,
    db_name="test_db",
    collection_name="test_collection",
):
    raise NotImplementedError


def find_many(
    client: MongoClient,
    condition: Dict,
    db_name="test_db",
    collection_name="test_collection",
) -> Cursor:
    raise NotImplementedError


def set_new_value(
    client: MongoClient,
    contidion,
    field,
    new_value,
    create_new: bool,
    db_name="test_db",
    collection_name="test_collection",
) -> InsertOneResult:
    raise NotImplementedError
