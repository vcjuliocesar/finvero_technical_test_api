from fastapi import HTTPException,status,Depends
from fastapi.security import HTTPBearer
from starlette.requests import Request
from datetime import datetime
from src.infrastructure.exceptions.invalid_credentials_exception import InvalidCredentialsException
#from src.infrastructure.exceptions.utils import get_http_exception
from src.infrastructure.utils.jwt_utils import validate_token
#from src.services.user_service import UserService


class JWTBearer(HTTPBearer) :
    
    async def __call__(self, request: Request):
        
        
        try:
            
            auth = await super().__call__(request)
            
            credential = validate_token(auth.credentials)
            
            expire = datetime.fromtimestamp(credential['exp'])
            
            if credential['email'] != 'jhon.doe@example.com':
                
                raise InvalidCredentialsException()
            
            if expire is None:
                
                raise InvalidCredentialsException()
            
            return 'finvero'
    
        except Exception as error:
            
            raise error