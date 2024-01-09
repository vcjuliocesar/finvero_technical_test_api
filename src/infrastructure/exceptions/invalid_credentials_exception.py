class InvalidCredentialsException(Exception):
    
    def __init__(self, message:str = "Invalid Credentials") -> None:
        
        self.message = message
        
        super().__init__(self.message)