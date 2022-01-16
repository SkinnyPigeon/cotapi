import sys
# import pytest

if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]

from transaction_functions import TransactionFunctions
from transaction_persistance import TransactionPersistance

address = "51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23"

def test_can_retrieve_all_transactions():
    tf = TransactionFunctions(address, "test")
    trans = tf.retrieve_transactions()
    assert len(trans) > 0
    assert set(list(trans[0].keys())) == set(["_id",
                                              "amount",
                                              "fee",
                                              "sender",
                                              "receiver",
                                              "date",
                                              "type",
                                              "description",
                                              "transactionDetails"
                                              ])

def test_can_limit_number_of_transactions():
    tf = TransactionFunctions(address, "test")
    trans = tf.retrieve_last_x_transactions(-1, 1)
    assert len(trans) == 1

def test_can_retrieve_transaction_by_hash():
    tp = TransactionPersistance("test", [{"_id": "abc", "amount": 123}])
    tp.save_transactions()
    tf = TransactionFunctions(address, "test")
    tran = tf.transaction_by_id("abc")
    assert tran == {"_id": "abc", "amount": 123}


sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")
