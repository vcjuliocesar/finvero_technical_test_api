from fastapi import HTTPException,status,Depends
from fastapi.security import HTTPBearer
from starlette.requests import Request
from datetime import datetime
from src.infrastructure.exceptions.http_exception import get_http_exception
from src.infrastructure.exceptions.invalid_credentials_exception import InvalidCredentialsException
#from src.infrastructure.exceptions.utils import get_http_exception
from src.infrastructure.utils.jwt_utils import validate_token
from src.service.user_service import UserService


class JWTBearer(HTTPBearer) :
    
    async def __call__(self, request: Request,user_service:UserService = Depends()):
        
        self.user_service = user_service
        
        try:
            
            auth = await super().__call__(request)
            
            credential = validate_token(auth.credentials)
            
            expire = datetime.fromtimestamp(credential['exp'])
            
            user = self.user_service.find_one({"email":credential['email']})
            
            
            if not user:
                
                raise InvalidCredentialsException()
            
            if expire is None:
                
                raise InvalidCredentialsException()
            
            return user
    
        except Exception as error:
            
            raise get_http_exception(error)