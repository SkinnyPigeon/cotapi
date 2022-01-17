from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
import json


class UpdatedTransactionResponse(BaseModel):
    detail: str = "Successfully inserted 10 new records"


class SavedTransactionRequestBody(BaseModel):
    start: Optional[datetime] = datetime.now() - timedelta(days=2)
    end: Optional[datetime] = datetime.now()
    direction: Optional[int] = -1


class XNumberOfTransactionsRequest(BaseModel):
    direction: int = -1
    limit: int = 3


class TransactionByHashRequest(BaseModel):
    tx_hash: str = "154859b2f3b07e901e17070a034a15fa3dba0cf1109dfd0680b0ac1d43b4caea"


class OutgoingsRequest(BaseModel):
    start: Optional[datetime] = datetime(1970, 1, 1)
    end: Optional[datetime] = datetime.now()


class OutgoingsResponse(BaseModel):
    outgoings: float = 2839182.1389


class IncomeRequest(BaseModel):
    start: Optional[datetime] = datetime(1970, 1, 1)
    end: Optional[datetime] = datetime.now()


class IncomeResponse(BaseModel):
    income: float = 7287328.123


class BalanceRequest(BaseModel):
    start: Optional[datetime] = datetime(1970, 1, 1)
    end: Optional[datetime] = datetime.now()


class BalanceResponse(BaseModel):
    balance: float = 4448145.9841
    income: float = 7287328.123
    outgoings: float = 2839182.1389



transactionDetails = json.loads('''[
      {
        "hash": "3f8831d0f3ec0f98a76791e04da9ea5141acdaacd52157cc247685f9b50e45a8",
        "addressHash": "0011acfb3db0e4dac0eebe657ec3eb0087c2c1fd738f5aa2234ce4569c8e8096064d03fa7bac56f5c4e662187fafd82ed85f60c30c98298cd3a49cd7735334f47b1aadd7",
        "amount": -2526.55803,
        "createTime": 1642089732.241,
        "name": "IBT"
      },
      {
        "hash": "f26f9e47a339ace8167d7141ff0ce260280300076437b78a7337924dac35eeae",
        "addressHash": "7eb3f689a14dec964e48d1c661f8a67d45db1d35add4d3df77a1f176195382f88c4d222298476de1d53bce553c6e88b2f163d665c990bb2fb25bf08b1728faa4f09cbdea",
        "amount": 2.521515,
        "createTime": 1642089731.672,
        "name": "FFBT",
        "originalAmount": 2521.515
      },
      {
        "hash": "9a6a6641243454509ead7da9fdaaf365c944399279e8677f1056e7851dcc4b00",
        "addressHash": "75d5c1381a021027017607dae51c73a0126688386c1ecb0fb98166ac55572ac43091fd4e3cd65b78f9deddb00445a269c2d392ad0e1dd04b1c87af712673aef06a524c1a",
        "amount": 2.521515,
        "createTime": 1642089732.19,
        "name": "NFBT",
        "originalAmount": 2521.515,
        "reducedAmount": null,
        "networkFeeTrustScoreNodeResult": [
          {
            "trustScoreNodeHash": "ea1aba58e78954715ac7f885ff3cb4a5af3e2f310fb0a96986da6fbd958c75791b1266ad38bd34d6bab725c5b23a29661dd424c47e5f9765990e363b2530fd5c",
            "trustScoreNodeSignature": {
              "r": "65cf82ab27ab92e0401f5296b6fa08f3597a5d46bf31b644345b7a2b748e3321",
              "s": "4143d3ab1eedd55339e96b7097d43fcb77f7154f8bbcce52d90dcd0e9140fd32"
            },
            "valid": true
          },
          {
            "trustScoreNodeHash": "ea1aba58e78954715ac7f885ff3cb4a5af3e2f310fb0a96986da6fbd958c75791b1266ad38bd34d6bab725c5b23a29661dd424c47e5f9765990e363b2530fd5c",
            "trustScoreNodeSignature": {
              "r": "ddf1b6a09d9b85d53b0a8ef208eca6412724b4e9557397c01447f1f89bf38a0e",
              "s": "4922e91ef58b790edc3de94a146914e047037adc346b418f67e374a9782bafc7"
            },
            "valid": true
          },
          {
            "trustScoreNodeHash": "ea1aba58e78954715ac7f885ff3cb4a5af3e2f310fb0a96986da6fbd958c75791b1266ad38bd34d6bab725c5b23a29661dd424c47e5f9765990e363b2530fd5c",
            "trustScoreNodeSignature": {
              "r": "bf4b64176403474da8ed6f206e9692c9b0af7db899f62bda98a4c38d2cbb6ca2",
              "s": "d93936b7cc7d1f55383d61bd0ab17a548c68b2146ca0e22a31f5898c03181d0a"
            },
            "valid": true
          }
        ]
      },
      {
        "hash": "67a3bbf4deb2c184a7b5acd4fd26e5f72ea6c4435fd563fd36f1a02d6a735b32",
        "addressHash": "51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23",
        "amount": 2521.515,
        "createTime": 1642089733.415,
        "name": "RBT",
        "originalAmount": 2521.515,
        "receiverDescription": null
      }
    ]''')


class IndividualTransaction(BaseModel):
    _id: str = "0f3384f5729899e5674984e8ed131e72264b2f1172fe4eebf95bbc7b88d5b693"
    amount: float = 2526.55803
    date: float = 1642089733.415
    description: str = "Payment"
    fee: float = 5.04303
    receiver: str = "51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23"
    sender: str = "0011acfb3db0e4dac0eebe657ec3eb0087c2c1fd738f5aa2234ce4569c8e8096064d03fa7bac56f5c4e662187fafd82ed85f60c30c98298cd3a49cd7735334f47b1aadd7"
    type: str = "Transfer"
    transactionDetails: list[dict] = transactionDetails


class SavedTransactionsResponse(BaseModel):
    __root__: list[IndividualTransaction]


class TokenResponse(BaseModel):
    access_token: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdGV2ZSIsImV4cCI6MTY0MjQxMTUzM30.FiHoo_GhZfkZe5SPlB0_LDzhOkocgLS-a7kW27ImLog"
    token_type: str = "bearer"