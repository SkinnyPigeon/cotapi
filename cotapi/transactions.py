import requests

class Transactions:
    def __init__(self, address):
        self._url = 'https://staycoti.betternode.net/transaction/addressTransactions'
        self._address = {"address": address}
        self._transactions = []
        self.get_transactions()

    def get_transactions(self):
        res = requests.post(self._url, json=self._address)
        raw_transactions = res.json()
        self._transactions = [self.format_transaction(transaction)
                              for transaction
                              in raw_transactions["transactionsData"]]

    def format_transaction(self, transaction):
        sender = [details["addressHash"] for details
                  in transaction["baseTransactions"]
                  if details["name"] == 'IBT'
                  ][0]
        receiver = [details["addressHash"] for details
                    in transaction["baseTransactions"]
                    if details["name"] == 'RBT'
                    ][0]
        fee = sum([details["amount"] for details
                   in transaction["baseTransactions"]
                   if details["name"] in ["FFBT", "NFBT"]
                   ])
        transaction = {
            "_id": transaction["hash"],
            "amount": transaction['amount'],
            "fee": fee,
            "sender": sender,
            "receiver": receiver,
            "date": transaction["createTime"],
            "type": transaction["type"],
            "description": transaction["transactionDescription"],
            "transactionDetails": transaction["baseTransactions"]
        }
        return transaction

    def return_transactions(self):
        return self._transactions