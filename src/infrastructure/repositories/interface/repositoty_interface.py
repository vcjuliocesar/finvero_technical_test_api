from abc import ABC, abstractmethod

class RepositoryInterface(ABC):
    
    @abstractmethod
    def create(self,data):
        pass
    
    @abstractmethod
    def find_by(self,criteria):
        pass
    
    @abstractmethod
    def delete(self,data):
        pass