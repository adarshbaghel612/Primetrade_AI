from pydantic import BaseModel,Field
from typing import Optional, Literal
from datetime import date

class Create(BaseModel):
    amount: float = Field(..., gt=0, description="Transaction amount")
    type: Literal["income", "expense"] = Field(..., description="Type of transaction")
    category: str = Field(..., min_length=1, max_length=100)
    Date: date = Field(..., description="Transaction date")
    notes: Optional[str] = Field(None, max_length=255, description="Optional description")

class Update(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    type: Optional[Literal["income", "expense"]] = None
    category: Optional[str] = Field(None, min_length=2, max_length=50)
    notes: Optional[str] = Field(None, max_length=255)

class ShowTask(Create):
    id:int
    
class Show(BaseModel):
    id:int
    amount:float
    type:str
    category:str
    Date:date
    notes:str

    model_config = {
        "from_attributes": True
    }
    




