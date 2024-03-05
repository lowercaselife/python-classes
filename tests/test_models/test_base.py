import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_update_attributes(self):
        obj = Base(1)
        obj.update_attributes(name="Alice", age=30)
        self.assertEqual(obj.name, "Alice")
        self.assertEqual(obj.age, 30)

    def test_set_id(self):
        obj = Base(1)
        obj.id = 2
        self.assertEqual(obj.id, 2)

    def test_to_json(self):
        obj = Base(1)
        obj.update_attributes(name="Alice", age=30)
        expected_json = '{"id": 1, "name": "Alice", "age": 30}'
        self.assertEqual(obj.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()

