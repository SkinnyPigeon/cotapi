from pymongo import MongoClient
from typing import Optional
from passlib.context import CryptContext

class UserPersistance:
    def __init__(self, username: str,
                 password: Optional[str] = None,
                 address: Optional[str] = None
                 ):
        self.username = username
        self.password = password
        self.address = address
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['users']
        self._collection = self._db['login']

    def create_user(self):
        if not self._collection.find_one({"username": self.username}):
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            password_to_store = pwd_context.hash(self.password)
            self._collection.insert_one({"username": self.username,
                                         "key": password_to_store,
                                         "disabled": False,
                                         "address": self.address})
            return True
        else:
            return False

    def delete_user(self):
        result = self._collection.delete_one({"username": self.username})
        return result