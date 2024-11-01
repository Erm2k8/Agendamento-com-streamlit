from models.client import Client, Clients
from models.schedules import Schedule, Schedules
from models.services import Service, Services
from datetime import time, datetime, timedelta
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
    def update_client(id, client: Dict):
        Clients.load_data()
        return Clients.update(id, client)
    
    @staticmethod
    def delete_client(id: int):
        Clients.load_data()
        return Clients.delete(id)
    
    @staticmethod
    def list_schedules():
        Schedules.load_data()
        return [s.to_dict() for s in Schedules.list()]

    @staticmethod    
    def insert_schedule(schedule: Dict):
        Schedules.load_data()
        return Schedules.create(schedule)
    
    @staticmethod
    def update_schedule(id, schedule: Dict):
        Schedules.load_data()
        return Schedules.update(id, schedule)
    
    @staticmethod
    def delete_schedule(id: int):
        Schedules.load_data()
        return Schedules.delete(id)

    @staticmethod
    def list_services():
        Services.load_data()
        return [s.to_dict() for s in Services.list()]
    
    @staticmethod
    def insert_service(service: Dict):
        Services.load_data()
        return Services.insert(Service.from_dict(service))
    
    @staticmethod
    def update_service(id, service: Dict):
        Services.load_data()
        return Services.update(id, service)
    
    @staticmethod
    def delete_service(id: int):
        Services.load_data()
        return Services.delete(id)