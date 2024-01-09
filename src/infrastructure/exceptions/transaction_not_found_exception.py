class TransactionNotFoundException(Exception):
    
    def __init__(self, message:str = "Transaction not found") -> None:
        
        self.message = message
        
        super().__init__(self.message)