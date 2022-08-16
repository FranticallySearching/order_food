import uuid

import pytest

import utils.db.mongo


@pytest.fixture()
def mongo_client():
    print("setup")
    localhost_kwargs = {
        "alias": uuid.uuid4().hex,
        "db": "mongoenginetest",
        "host": "mongomock://localhost",
    }
    client = utils.db.mongo.connect(**localhost_kwargs)
    try:
        yield client
    finally:
        client.close()
    print("teardown")


def test_connection(mongo_client):
    assert mongo_client.list_database_names(), "Failed to connect to Mongo! Couldn't find any database names!"
