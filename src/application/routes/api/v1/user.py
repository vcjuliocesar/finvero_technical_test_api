from fastapi import HTTPException,APIRouter,status,Depends
from fastapi.responses import JSONResponse
from src.application.usecases.create_user_use_case import CreateUserUseCase
from src.application.usecases.find_by_email_user_use_case import FindByEmailUserUseCase
from src.infrastructure.exceptions.http_exception import get_http_exception
from src.infrastructure.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.infrastructure.schemas.user_schema import UserAuthRequest, UserPostRequest, UserSchema
from src.infrastructure.exceptions.user_not_found_exception import UserNotFoundException
from src.infrastructure.utils.jwt_utils import create_token
from src.infrastructure.utils.password_utils import PasswordUtils

user_router = APIRouter(prefix="/api/v1",tags=['Users'])

@user_router.post("/users",response_model=UserSchema,status_code=status.HTTP_200_OK)
async def create(user:UserPostRequest,user_case:CreateUserUseCase = Depends()):
    
    try:
        
        user_case.execute(user)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"User created"})
    
    except UserAlreadyExistsException as error:
        
        raise get_http_exception(error)
        
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))