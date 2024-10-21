from models.client import Client, Clients
from typing import Dict

class View:
    @staticmethod
    def list_clients():
        Clients.load_data()
        return [c.to_dict() for c in Clients.list()]
    
    @staticmethod
    def insert_client(client: Dict):
        Clients.load_data()
        return Clients.insert(Client.from_dict(client))
    
    @staticmethod
    def update_client(id):
        Clients.load_data()
        return Clients.update(id)
    
    @staticmethod
    def delete_client(id: int):
        Clients.load_data()
        return Clients.delete(id)
