import sys
import random
import string
if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]

from transaction_persistance import TransactionPersistance
import datetime

address = "51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23"


def test_can_save_transactions_to_db():
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
            "amount": 12.2,
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
    assert tp.get_update_count() == 2


sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")
