import json

class Base:
    instances = {}

    def __init__(self, id, *args, **kwargs):
        self._id = id
        Base.instances[id] = self
        self.update_attributes(*args, **kwargs)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id
        self.update_json()

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def to_json(self):
        return json.dumps({'id': self.id, **self.__dict__})

    @classmethod
    def from_json(cls, json_str):
        try:
            data = json.loads(json_str)
            instance = cls(data['id'], **data)
            return instance
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error occurred while deserializing JSON: {e}")
            return None

    def update_json(self):
        try:
            all_instances_json = [obj.to_json() for obj in Base.instances.values()]
            with open('instances.json', 'w') as f:
                json.dump(all_instances_json, f)
        except Exception as e:
            print(f"Error occurred while updating JSON file: {e}")

    def update_attributes(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
