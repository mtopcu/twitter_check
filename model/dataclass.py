from dataclasses import dataclass
from typing import List

'''Follow Request Response'''
@dataclass
class User:
  id: str
  name: str
  username: str

@dataclass
class Meta:
  result_count: int
  next_token: str = None
  previous_token: str = None
  
@dataclass
class Response:
    data: List[User]
    meta: Meta
    
'''Username Request Response'''    
@dataclass
class Username:
    data: User
