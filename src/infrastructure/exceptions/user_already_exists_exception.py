class UserAlreadyExistsException(Exception):
    
    def __init__(self, message:str = "User already exists") -> None:
        
        self.message = message
        
        super().__init__(self.message)