import json
from typing import List, Dict

class JSONDAO:
    def __init__(self, path: str) -> None:
        self.path = path

    def load(self):
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    def save(self, data: List[Dict]):
        try:
            with open(self.path, 'w') as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            pass

    def create(self, obj: Dict):
        data = self.load()
        data.append(obj)
        self.save(data)
    
    def delete(self, id: int):
        data = self.load()
        data = [obj for obj in data if obj['id'] != id]
        self.save(data)
    
    def update(self, obj: Dict):
        data = self.load()
        for i in range(len(data)):
            if data[i]['id'] == obj['id']:
                data[i] = obj
                break
            