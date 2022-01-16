import sys
if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]
import datetime
import random
import string
from transaction_persistance import TransactionPersistance

address = "51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23"
epoch = datetime.datetime(1970, 1, 1)
now = datetime.datetime.now()
utc = (now - epoch).total_seconds()
transactions = [
    {
        "_id": "".join((random.choice(string.ascii_lowercase)
                        for _ in range(20))),
        "amount": 12.2,
        "fee": 1,
        "sender": address,
        "receiver": "bar",
        "date": utc,
        "type": "transaction",
        "description": "transaction",
        "transactionDetails": {}
    },
    {
        "_id": "".join((random.choice(string.ascii_lowercase)
                        for _ in range(20))),
        "amount": 20,
        "fee": 1,
        "sender": 'foo',
        "receiver": address,
        "date": utc,
        "type": "transaction",
        "description": "transaction",
        "transactionDetails": {}
    }
]
tp = TransactionPersistance("test", transactions)
tp.save_transactions()

sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")
