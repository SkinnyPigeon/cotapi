from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta


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