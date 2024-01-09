class AccountNotFoundException(Exception):
    
    def __init__(self, message:str = "Account no exists") -> None:
        
        self.message = message
        
        super().__init__(self.message)