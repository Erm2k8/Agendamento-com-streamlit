import re
from .abstract_dao import AbstractDAO
from .json_dao import JSONDAO as json_dao
from typing import List, Dict

class Client:
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def __init__(self, id: int, name: str, email: str, phone: str):
        self.__id = 0
        self.__name = ""
        self.__email = ""
        self.__phone = ""

        self.set_id(id)
        self.set_name(name)
        self.set_email(email)
        self.set_phone(phone)

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_phone(self) -> str:
        return self.__phone
    
    def set_id(self, id: int):
        if isinstance(id, int) and id >= 0:
            self.__id = id
        else:
            raise ValueError("Invalid id")
    
    def set_name(self, name: str):
        if isinstance(name, str) and len(name) > 0 and name.replace(" ", "").isalpha():
            self.__name = name
        else:
            raise ValueError("Invalid name")
    
    def set_email(self, email: str):
        if isinstance(email, str) and re.match(self.email_regex, email):
            self.__email = email
        else:
            raise ValueError("Invalid email")
    
    def set_phone(self, phone: str):
        if isinstance(phone, str) and 12 > len(phone) > 0 and phone.replace(" ", "").isdigit():
            self.__phone = phone
        else:
            raise ValueError("Invalid phone")
        
    def to_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'phone': self.__phone
        }
    
    @staticmethod
    def from_dict(data: Dict):
        return Client(
            data['id'],
            data['name'],
            data['email'],
            data['phone']
        )
        
    def __str__(self) -> str:
        return f"{self.__id} {self.__name} {self.__email} {self.__phone}"
    

class Clients(AbstractDAO):
    clients: List[Client] = []
    dao = json_dao("./data/clients.json")
    
    if dao.load():
        for client in dao.load():
            clients.append(Client.from_dict(client))

    @classmethod
    def load_data(cls):
        cls.clients = []
        data = cls.dao.load()
        if data:
            for client in data:
                cls.clients.append(Client.from_dict(client))

    @classmethod
    def save_data(cls):
        data = []
        for client in cls.clients:
            data.append(client.to_dict())
        cls.dao.save(data)

    @classmethod
    def list(cls):
        cls.load_data()
        return cls.clients

    @classmethod
    def insert(cls, client: Client):
        cls.load_data()

        print(max([c['id'] for c in [c.to_dict() for c in cls.clients]]) + 1)

        print(c.to_dict() for c in cls.clients)

        next_id = max([c['id'] for c in (c.to_dict() for c in cls.clients)], default=0) + 1
    
        client.set_id(next_id)
        
        cls.clients.append(client)
        cls.save_data()

    def update(self, client: Client):
        self.load_data()
        for index, c in enumerate(self.clients):
            if c.get_id() == client.get_id():
                self.clients[index] = client
                break
        self.save_data()

    def delete(self, id: int):
        self.load_data()
        for index, c in enumerate(self.clients):
            if c.get_id() == id:
                del self.clients[index]
                break
        self.save_data()

    def get_by_id(self, id: int):
        self.load_data()
        for c in self.clients:
            if c.get_id() == id:
                return c
        return None
    