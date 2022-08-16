import os
from typing import Optional

import mongoengine

import utils.dotenv


def connect(*, alias: Optional[str] = None, **kwargs) -> mongoengine.connection.MongoClient:
    """Register a connection to MongoDB
    kwargs:
      serverSelectionTimeoutMS (int): Milliseconds for connection timeout
    """
    if not kwargs:
        kwargs = {}
    if alias:
        kwargs["alias"] = alias

    utils.dotenv.read_dotenv()

    kwargs.update({
        "db": os.environ['MONGO_DATABASE'],
        "host": get_host(os.environ['MONGO_USERNAME'], os.environ['MONGO_PASSWORD'], os.environ['MONGO_HOST'])
    })
    client = mongoengine.connect(**kwargs)
    assert client.get_database(kwargs["db"]).name, f"Failed to connect to MongoDB properly"
    return client


def get_host(username: str, password: str, host: str) -> str:
    return f"mongodb+srv://{username}:{password}@{host}"
