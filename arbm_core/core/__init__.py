from pymongo import MongoClient
from dotenv import dotenv_values

__all__ = ["MongoDb"]

config = dotenv_values(".env")


_mongodb_client = MongoClient(config["MONGO_ATLAS_URI"], uuidRepresentation="standard")
MongoDb = _mongodb_client[config["MONGO_ATLAS_DB_NAME"]]
