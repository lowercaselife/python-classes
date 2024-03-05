import unittest
from models.person import Person

class TestPerson(unittest.TestCase):
    def test_init(self):
        person = Person(1, "Alice", 30)
        self.assertEqual(person.id, 1)
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 30)

    def test_set_name(self):
        person = Person(1, "Alice", 30)
        person.name = "Bob"
        self.assertEqual(person.name, "Bob")

    def test_set_age(self):
        person = Person(1, "Alice", 30)
        person.age = 40
        self.assertEqual(person.age, 40)

    def test_from_json(self):
        json_data = '{"id": 1, "name": "Alice", "age": 30}'
        person = Person.from_json(json_data)
        self.assertEqual(person.id, 1)
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 30)

if __name__ == '__main__':
    unittest.main()
