import unittest
from collection.Array import Array

class ArrayTest(unittest.TestCase):
      def test_that_Array_length_method_exist(self):
          array = Array(3)
          self.assertEqual(len(array), array.__len__())

      def test_that_Array_size_exists(self):
        array = Array(5)
        self.assertEqual(array.__len__(), 5)

      def test_that_Array_fill_method_exists(self):
          array = Array(3)
          array._fill(-1)
          answer = Array(3)
          answer._fill(-1)
          self.assertEqual(array.get(), answer.get())

      def test_that_Array_contains_item(self):
          array = Array(5)
          array._fill(3)
          self.assertEqual(array.contains(3), True)

      def test_that_Array_CopyOfMethod_exists(self):
          array = Array(3)
          array._fill(2)
          answer = array.copy_of_array(3)
          self.assertEqual(array.get(), answer.get())

      def test_that_Array_Is_Iterable(self):
          array = Array(3)
          array._fill(3)
          iterator = [item for item in array]
          self.assertListEqual(iterator, [3,3,3])