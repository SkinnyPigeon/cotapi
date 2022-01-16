from pymongo import MongoClient


class TransactionPersistance:
    def __init__(self,
                 collection_name: str,
                 transactions: list):
        self._collection_name = collection_name
        self._transactions = transactions
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['transactions']
        self._collection = self._db[self._collection_name]
        self._ids = []

    def save_transactions(self):
        for transaction in self._transactions:
            id = self._collection.update_one({"_id": transaction["_id"]},
                                             {"$setOnInsert": transaction},
                                             upsert=True
                                             )
            if id.upserted_id is not None:
                self._ids.append(id)

    def get_update_count(self):
        return len(self._ids)
