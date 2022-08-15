import os
import pathlib
from typing import NoReturn

import dotenv


def read_dotenv() -> NoReturn:
    """Raises False if it fails to load an expected key in the .env file"""
    dotenv.read_dotenv(str(pathlib.Path(__file__).parent.parent.joinpath(".env")))
    assert os.environ.get("MONGO_DATABASE") is not None, "Didn't load the .env file appropriately"
