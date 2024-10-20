from abc import ABC, abstractmethod

class AbstractDAO(ABC):
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass
    
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def get(self, id):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, id, data):
        pass