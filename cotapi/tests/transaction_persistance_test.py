import sys
import random  
import string  
if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]

from transaction_persistance import TransactionPersistance


def test_can_save_transactions_to_db():
    transactions = [
        {
            "_id": "".join((random.choice(string.ascii_lowercase)
                            for _ in range(20))),
            "amount": 12.2,
            "fee": 1,
            "sender": 'foo',
            "receiver": "bar",
            "date": "12/12/12",
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
            "receiver": "bar",
            "date": "12/12/12",
            "type": "transaction",
            "description": "transaction",
            "transactionDetails": {}
        }
    ]
    tp = TransactionPersistance("test", transactions)
    tp.save_transactions()
    assert tp.get_update_count() == 2


sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")
