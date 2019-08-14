import functools

import pymongo
import random
from src.db_worker import get_client
import pytest
from pymongo import MongoClient
import mongomock


@pytest.fixture
def mock_mongo():
    return mongomock.MongoClient()


servers = ["server.example.com", "server2.example.com"]
ports = [27017, 27024]
invalid_ports = map(str, ports)


@pytest.fixture
def test_data():
    return random.choice(
        [
            {
                "name": "Temp name 1",
                "parameters": {"location": "Innopolis", "value": 7},
            },
            {
                "name": "Temp name 2",
                "parameters": {"location": "Innopolis", "value": 3},
            },
            {"name": "Temp name 3", "parameters": {"location": "Kazan", "value": 7}},
            {"name": "Temp name 4", "parameters": {"location": "Kazan", "value": 5}},
        ]
    )


def my_params(func):
    @functools.wraps(func)
    @pytest.mark.parametrize("server_name", servers)
    @pytest.mark.parametrize("port", ports)
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapped


class TestBasicConnection:
    @my_params
    def test_establishing_invalid_connection(self, server_name, port, test_data):
        with pytest.raises(pymongo.errors.ServerSelectionTimeoutError):
            client = get_client(server_name, port, serverSelectionTimeoutMS=1)
            client.test_db.collect.insert_one(test_data)

    @pytest.mark.parametrize("server_name", servers)
    @pytest.mark.parametrize("port", invalid_ports)
    def test_invalid_ports(self, server_name, port):
        with pytest.raises(TypeError):
            client = get_client(server_name, port, serverSelectionTimeoutMS=1)

    @my_params
    def test_client_connection(self, server_name, port):
        client1 = get_client(server_name, port)
        assert isinstance(client1, MongoClient)

        client2 = get_client(server_name, port)
        assert client1 is client2

        new_server_name, new_port = random.choice(zip(servers, ports))
        # if I put new (host, port) it should be an error

        with pytest.raises(
            ValueError
        ):  # if I got new server&port combination, it should be not allowed
            _ = get_client(new_server_name, new_port)
