import unittest
from collection.set import my_set

class MySet(unittest.TestCase):
      def test_MySet_length(self):
          my_set1 = my_set([1,2,3])
          self.assertEqual(my_set1.__len__(), 3)