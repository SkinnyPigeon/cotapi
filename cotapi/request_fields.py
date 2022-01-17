from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta

class SavedTransactionRequestBody(BaseModel):
    start: Optional[datetime] = datetime.now() - timedelta(days=2)
    end: Optional[datetime] = datetime.now()
    direction: Optional[int] = -1