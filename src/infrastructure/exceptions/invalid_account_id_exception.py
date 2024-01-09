class InvalidAccountIdException(Exception):
    
    def __init__(self, message:str = "Invalid Account id") -> None:
        
        self.message = message
        
        super().__init__(self.message)