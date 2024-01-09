from fastapi import HTTPException,APIRouter,status,Depends
from fastapi.responses import JSONResponse
from src.infrastructure.schemas.user_schema import UserAuthRequest
from src.infrastructure.exceptions.user_not_found_exception import UserNotFoundException
from src.infrastructure.utils.jwt_utils import create_token
from src.infrastructure.utils.password_utils import PasswordUtils

auth_router = APIRouter(prefix="/api/v1",tags=["Auth"])

@auth_router.post('/login',status_code=status.HTTP_200_OK)
async def login(user:UserAuthRequest):
    
    utils = PasswordUtils()
    
    try:
        
        token = "holi"
        
        #print(utils.hash_password(user.password))
        if not utils.verify_password(user.password,"$2b$12$SGEEfM5GzcJFlD0LmeJIm.4k5iBlzbl9jH40v9H69djFmBsCTTFEu"):
            
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"message":"Unauthorized"})    
        
        token = create_token(user.model_dump())
        
        return JSONResponse(status_code=status.HTTP_200_OK,content=token)
        
        
    except UserNotFoundException as error:
        
        raise error
    
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))