import re
from .abstract_dao import AbstractDAO
from .json_dao import JSONDAO as json_dao
from typing import List, Dict
from datetime import datetime as dt

class Schedule:
    def __init__(self, id: int, client_id: int, service_id: int, data: dt, confirmed: bool):
        self.__id = 0
        self.__client_id = 0
        self.__service_id = 0
        self.__data = dt.now()
        self.__confirmed = False

        self.set_id(id)
        self.set_client_id(client_id)
        self.set_service_id(service_id)
        self.set_data(data)
        self.set_confirmed(confirmed)

    def get_id(self) -> int:
        return self.__id

    def get_client_id(self) -> int:
        return self.__client_id

    def get_service_id(self) -> int:
        return self.__service_id

    def get_data(self) -> dt:
        return self.__data

    def get_confirmed(self) -> bool:
        return self.__confirmed
    
    def set_id(self, id: int):
        if isinstance(id, int) and id >= 0:
            self.__id = id
        else:
            raise ValueError("Invalid id")
        
    def set_client_id(self, client_id: int):
        if isinstance(client_id, int) and client_id >= 0:
            self.__client_id = client_id
        else:
            raise ValueError("Invalid client_id")
        
    def set_service_id(self, service_id: int):
        if isinstance(service_id, int) and service_id >= 0:
            self.__service_id = service_id  
        else:
            raise ValueError("Invalid service_id")
        
    def set_data(self, data: dt):
        if isinstance(data, dt):
            self.__data = data
        else:
            raise ValueError("Invalid data")

    def set_confirmed(self, confirmed: bool):
        if isinstance(confirmed, bool):
            self.__confirmed = confirmed
        else:
            raise ValueError("Invalid confirmed")
        
    def to_dict(self) -> Dict:
        return {
            "id": self.__id,
            "client_id": self.__client_id,
            "service_id": self.__service_id,
            "data": self.__data,
            "confirmed": self.__confirmed
        }

    @staticmethod
    def from_dict(data: Dict) -> "Schedule":
        return Schedule(
            data["id"],
            data["client_id"],
            data["service_id"],
            data["data"],
            data["confirmed"]
        )
    
    def __str__(self) -> str:
        return f"Schedule(id={self.__id}, client_id={self.__client_id}, service_id={self.__service_id}, data={self.__data}, confirmed={self.__confirmed})"
    

class Schedules(AbstractDAO):
    schedules: List[Schedule] = []
    dao = json_dao("./data/schedules.json")

    @classmethod
    def load_data(cls):
        cls.schedules = []
        data = cls.dao.load()
        if data:
            for schedule in data:
                cls.schedules.append(Schedule.from_dict(schedule))

    @classmethod
    def save_data(cls):
        data = [schedule.to_dict() for schedule in cls.schedules]
        cls.dao.save(data)

    @classmethod
    def create(cls, data):
        schedule = Schedule.from_dict(data)
        cls.schedules.append(schedule)
        cls.save_data()

    @classmethod
    def update(cls, id, data):
        schedule = Schedule.from_dict(data)
        for i, existing_schedule in enumerate(cls.schedules):
            if existing_schedule.get_id() == id:
                cls.schedules[i] = schedule
                cls.save_data()
                break

    @classmethod
    def delete(cls, id):
        for i, existing_schedule in enumerate(cls.schedules):
            if existing_schedule.get_id() == id:
                del cls.schedules[i]
                cls.save_data()
                break

    @classmethod
    def get_by_id(cls, id: int):
        return next((schedule for schedule in cls.schedules if schedule.get_id() == id), None)

    @classmethod
    def list(cls):
        return cls.schedules
