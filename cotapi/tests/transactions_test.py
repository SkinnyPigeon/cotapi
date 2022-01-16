import sys
import pytest
if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]
from transactions import Transactions

@pytest.mark.skip(reason="This passes but takes a long time to run")
def test_can_get_transactions():
    trans = Transactions('51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23')
    results = trans.return_transactions()
    assert len(results) > 0
    assert list(results[0].keys()) == ["_id", "amount", "fee", "sender", "receiver", "date", "type", "description", "transactionDetails"]

sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")