# check data structure
from pydantic import BaseModel

class IPCheck(BaseModel):
  ip: str

class URLCheck(BaseModel):
    url: str