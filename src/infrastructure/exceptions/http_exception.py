from fastapi import HTTPException,status

def get_http_exception(exception:Exception) -> HTTPException:
    
    status_code = exception.status_code if hasattr(exception,"status_code") else status.HTTP_500_INTERNAL_SERVER_ERROR
    
    return HTTPException(status_code=status_code,detail=str(exception))