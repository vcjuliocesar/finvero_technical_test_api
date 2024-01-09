from jwt import encode,decode
from datetime import datetime,timedelta
from src.infrastructure.config.enviroment import get_enviroment_settinngs

env = get_enviroment_settinngs()

def create_token(data:dict) -> dict:
    
    payload = expire_token(data)
    
    token:str = encode(payload,key=env().MY_SECRET_KEY,algorithm="HS256")
    
    return token

def validate_token(token:str) -> dict :
    
    data:dict = decode(token,key=env().MY_SECRET_KEY,algorithms=["HS256"])
    
    return data

def expire_token(data:dict):
    
    to_encode = data.copy()
    
    token_expires = timedelta(minutes=env().TOKEN_EXPIRE_MINUTES)
    
    expire = datetime.utcnow() + token_expires
    
    to_encode.update({'exp':expire})
    
    return to_encode