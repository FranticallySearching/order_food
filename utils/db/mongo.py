import os
import uuid
from typing import Optional

import mongoengine


def connect(**kwargs) -> mongoengine.connection.MongoClient:
    """Register a connection to MongoDB
    kwargs:
      serverSelectionTimeoutMS (int): Milliseconds for connection timeout
    """
    if not kwargs:
        kwargs = {}

    mongo_env_vars = {key.lower(): os.environ.get(f"MONGO_{key}")
                      for key in ("DB", "HOST", "USERNAME", "PASSWORD")
                      if os.environ.get(f"MONGO_{key}")}
    kwargs["host"] = kwargs.get("host", get_host(**mongo_env_vars))
    kwargs["db"] = kwargs.get("db", mongo_env_vars["db"])
    kwargs["alias"] = kwargs.get("alias", uuid.uuid4().hex)
    return mongoengine.connect(**kwargs)


def get_host(username: str, password: str, host: str, mongo_uri: Optional[str] = "mongodb+srv", **_) -> str:
    return f"{mongo_uri}://{username}:{password}@{host}"


def get_local_host_connection():
    localhost_kwargs = {
        "db": "mongoenginetest",
        "host": "mongomock://localhost",
    }
    return connect(**localhost_kwargs)
