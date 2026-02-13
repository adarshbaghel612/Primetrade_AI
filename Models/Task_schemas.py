from pydantic import BaseModel
from typing import Optional

class Create(BaseModel):
    Task:str
    Description:str

class Update(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ShowTask(Create):
    id:int
    
class Show(BaseModel):
    id:int
    task:str
    description:str

    model_config = {
        "from_attributes": True
    }
    




