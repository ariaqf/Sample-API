from abc import ABC, abstractmethod

class BaseSource(ABC):
    @abstractmethod
    def save(self, p):
        pass

    @abstractmethod
    def delete(self, id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get(self, id):
        pass
    
    @abstractmethod
    def get_by_name(self, name):
        pass