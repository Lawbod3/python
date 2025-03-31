import unittest
from collection.tuple import my_tuple

class TestMyTuple(unittest.TestCase):
    def test_my_tuple_length(self):
        tuple1 = my_tuple(1,2,3)
        self.assertEqual(tuple1.length_my_tuple(), 3)

    def test_my_tuple_contains_value(self):
        tuple1 = my_tuple(1,2,3)
        tuple1.contains_value(1)
        self.assertEqual(tuple1.contains_value(1), True)

    def test_my_tuple_getvalue(self):
        tuple1 = my_tuple(1,2,3)
        self.assertEqual(tuple1.getvalue(2), 3)



