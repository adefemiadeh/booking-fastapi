from pydantic import BaseModel
import uuid
from datetime import datetime, date

# Pydantic Model
class Book(BaseModel):
    uid:uuid.UUID
    title:str
    author:str
    publisher: str
    published_date:date
    page_count:int
    language:str
    created_at: datetime
    update_at: datetime


# Pydantic Model
class BookCreateModel(BaseModel):
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str

# Pydantic Model
class BookUpdateModel(BaseModel):
    title:str
    author:str
    publisher:str
    page_count:int
    language:str