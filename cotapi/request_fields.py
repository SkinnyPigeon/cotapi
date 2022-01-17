from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta


class SavedTransactionRequestBody(BaseModel):
    start: Optional[datetime] = datetime.now() - timedelta(days=2)
    end: Optional[datetime] = datetime.now()
    direction: Optional[int] = -1


class XNumberOfTransactionsRequest(BaseModel):
    direction: int = -1
    limit: int = 3


class TransactionByHashRequest(BaseModel):
    tx_hash: str = "154859b2f3b07e901e17070a034a15fa3dba0cf1109dfd0680b0ac1d43b4caea"