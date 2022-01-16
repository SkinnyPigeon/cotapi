from pymongo import MongoClient
import datetime


class TransactionFunctions:
    def __init__(self, address: str,
                 collection_name: str):
        self._address = address
        self._collection_name = collection_name
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['transactions']
        self._collection = self._db[self._collection_name]
        self.income = 0
        self.outgoings = 0

    def retrieve_transactions(self,
                              start: datetime.datetime = datetime.datetime(1970, 1, 1),
                              end: datetime.datetime = datetime.datetime.now(),
                              direction: int = -1):
        epoch = datetime.datetime(1970, 1, 1)
        start_utc = (start - epoch).total_seconds()
        end_utc = (end - epoch).total_seconds()
        transactions = list(self._collection.
                            find({"date": {
                                "$gte": start_utc,
                                "$lte": end_utc
                                }}).sort("date", direction).
                            allow_disk_use(True))
        return transactions
