import re
from .abstract_dao import AbstractDAO
from .json_dao import JSONDAO as json_dao
from typing import List, Dict

class Service:
    def __init__(self, id: int, description: str, price: float, duration: int):
        self.__id = 0
        self.__description = ""
        self.__price = 0
        self.__duration = 0

        self.set_id(id)
        self.set_description(description)
        self.set_price(price)
        self.set_duration(duration)

    def get_id(self) -> int:
        return self.__id

    def get_description(self) -> str:
        return self.__description

    def get_price(self) -> float:
        return self.__price

    def get_duration(self) -> int:
        return self.__duration
    
    def set_id(self, id: int):
        if isinstance(id, int) and id >= 0:
            self.__id = id
        else:
            raise ValueError("Invalid id")
        
    def set_description(self, description: str):
        if isinstance(description, str) and len(description) > 0:
            self.__description = description
        else:
            raise ValueError("Invalid description")

    def set_price(self, price: float):
        if isinstance(price, float) and price > 0:
            self.__price = price
        else:
            raise ValueError("Invalid price")

    def set_duration(self, duration: int):
        if isinstance(duration, int) and duration > 0:
            self.__duration = duration
        else:
            raise ValueError("Invalid duration")
        
    def to_dict(self) -> Dict:
        return {
            'id': self.__id,
            'description': self.__description,
            'price': self.__price,
            'duration': self.__duration
        }

    @staticmethod
    def from_dict(data: Dict):
        return Service(
            id=data.get('id', 0),
            description=data.get('description', ''),
            price=data.get('price', 0.0),
            duration=data.get('duration', 0)
        )

    def __str__(self) -> str:
        return f"{self.__id} {self.__description} {self.__price} {self.__duration}" 
    
class Services(AbstractDAO):
    services: List[Service] = []
    dao = json_dao("./data/services.json")
    
    if dao.load():
        for service in dao.load():
            services.append(Service.from_dict(service))

    @classmethod
    def load_data(cls):
        cls.services = []
        data = cls.dao.load()
        if data:
            for service in data:
                cls.services.append(Service.from_dict(service))

    @classmethod
    def save_data(cls):
        data = [service.to_dict() for service in cls.services]
        cls.dao.save(data)

    @classmethod
    def list(cls):
        cls.load_data()
        return cls.services

    @classmethod
    def insert(cls, service: Service):
        cls.load_data()
        next_id = max((s.get_id() for s in cls.services), default=0) + 1
        service.set_id(next_id)
        
        cls.services.append(service)
        cls.save_data()

    @classmethod
    def update(cls, id: int, service: Dict):    
        cls.load_data()
        for index, s in enumerate(cls.services):
            if s.get_id() == id:
                cls.services[index] = Service.from_dict(service)
                cls.save_data()
                break

    @classmethod
    def delete(cls, id: int):
        cls.load_data()
        cls.services = [s for s in cls.services if s.get_id() != id]
        cls.save_data()

    @classmethod
    def get_by_id(cls, id: int):
        cls.load_data()
        for s in cls.services:
            if s.get_id() == id:
                return s
        return None
