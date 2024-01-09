from passlib.context import CryptContext

class PasswordUtils():
    
    def __init__(self) -> None:
        
        self.pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
    
    def hash_password(self,password:str):
    
        return self.pwd_context.hash(password)

    def verify_password(self,password:str,hash:str):
    
        return self.pwd_context.verify(password,hash)
    
    