from models.base import Base
from models.person import Person
import json
# Create instances of Person class
person1 = Person(1, "Alice", 30)
person2 = Person(2, "Bob", 25)
person3 = Person(3, "Charlie", 40)
print(person1.__dict__.itemss())
print(Base.instances.items())
person1.id = 5
def file_storage():
    try:
        person_info = []
        for instance_id, instance in Base.instances.items():
            if isinstance(instance, Person):
                person_info.append(instance.to_json())

        with open('person_info.json', 'w') as f:
            json.dump(person_info, f, indent=4)
    except Exception as e:
        print(f"Error occurred while printing person info: {e}")

# Example usage:
file_storage()