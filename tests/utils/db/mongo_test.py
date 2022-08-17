import uuid

import utils.db.mongo


def test_connection():
    localhost_kwargs = {
        "alias": uuid.uuid4().hex,
        "db": "mongoenginetest",
        "host": "mongomock://localhost",
    }
    mongo_client = utils.db.mongo.connect(**localhost_kwargs)
    try:
        assert mongo_client.list_database_names(), "Failed to connect to Mongo! Couldn't find any database names!"
    finally:
        mongo_client.close()
