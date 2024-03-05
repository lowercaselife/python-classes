from models.base import Base
import json

class Person(Base):
    def __init__(self, id, name, age, *args, **kwargs):
        super().__init__(id, *args, **kwargs)
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, age={self.age})"

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}

    @classmethod
    def from_json(cls, json_str):
        try:
            data = json.loads(json_str)
            return cls(data['id'], data['name'], data['age'])
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error occurred while deserializing JSON: {e}")
            return None
