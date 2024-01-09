import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

@lru_cache
def get_env_file() -> str:
    env_file = os.getenv('ENV')
    return f".env.{env_file}" if env_file else ".env" 


class EnviromentSettings(BaseSettings):
    DATABASE_ENGINE:str
    DATABASE_NAME:str
    DATABASE_USER:str
    DATABASE_PASSWORD:str
    DATABASE_HOST:str
    DATABASE_PORT:int
    SECRETID:str
    SECRETPASSWORD:str
    LINKID:str
    BASE_URL:str
    
    class Config:
        env_file:str = get_env_file()
        
@lru_cache
def get_enviroment_settinngs():
    return EnviromentSettings;