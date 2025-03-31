import unittest
from collection.my_list import my_list

class TestMyList(unittest.TestCase):
      def test_MyList_add_element_to_list(self):
          my_list1 = my_list()
          self.assertEqual(my_list1.len(), 0)
          my_list1.append(1)
          self.assertEqual(my_list1.len(), 1)

      def test_MyList_length_method_to_get_list_size(self):
          my_list1 = my_list()
          self.assertEqual(my_list1.len(), 0)
          my_list2 = my_list()
          my_list2.append(1)
          my_list2.append(2)
          my_list2.append(3)
          self.assertEqual(my_list2.len(), 3)

      def test_MyList_remove_item_from_list(self):
          my_list1 = my_list()
          my_list1.append(1)
          my_list1.append(2)
          my_list1.append(3)
          self.assertEqual(my_list1.len(), 3)
          my_list1.remove(2)
          self.assertEqual(my_list1.len(), 2)

      def test_MyList_extend_another_list_into_It(self):
          my_list1 = my_list()
          my_list2 = my_list()
          my_list1.append(2)
          my_list1.append(2)
          self.assertEqual(my_list1.len(), 2)
          my_list2.append(2)
          my_list2.extend(my_list1)
          self.assertEqual(my_list2.len(), 3)

      def test_MyList_clear_All_elements(self):
          my_list1 = my_list()
          my_list1.append(1)
          my_list1.append(2)
          my_list1.clear()
          self.assertEqual(my_list1.len(), 0)






