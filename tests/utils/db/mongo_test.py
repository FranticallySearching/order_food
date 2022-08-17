import utils.db.mongo
import utils.dotenv


def test_connection():
    utils.dotenv.read_dotenv()
    mongo_client = utils.db.mongo.get_local_host_connection()
    try:
        is_localhost = mongo_client.host == "localhost"
        assert is_localhost, f"Failed to get localhost as host name!"
    finally:
        mongo_client.close()
