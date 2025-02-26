import unittest
import Todo


class TestValidateAddTaskFunction(unittest.TestCase):

      def test_that_validate_add_task_exist(self):
                Todo.validate_add_task(" ")


      def test_that_validate_add_task_correct_value(self):
                actual = Todo.validate_add_task(" ")
                result = False
                self.assertEqual(actual, result)


    
class TestValidateSelection(unittest.TestCase):

      def test_that_validate_selection_exist(self):
                selection = 5
                Todo.validate_selection(selection)

      def test_that_validate_selection_correct_value(self):
                selection = 5
                actual = Todo.validate_selection(selection)
                result = True
                self.assertEqual(actual, result)

class TestDeleteTask(unittest.TestCase):

      def test_that_delete_task_exist(self):
                selection = {'1': "bode", '2': "close", '3': "lawal"}
                Todo.delete_task(selection, 2)

      def test_that_delete_task_correct_value(self):
                selection = {'1': "bode", '2': "close", '3': "lawal"}
                actual = Todo.delete_task(selection, '2')
                result = {'1': "bode", '3': "lawal"}
                self.assertEqual(actual, result)

class TestCovertToString(unittest.TestCase):

      def test_that_convert_to_string_exist(self):
                Todo.convert_to_string(2)

      def test_that_convert_to_string_correct_value(self):
                actual = Todo.convert_to_string(2)
                result = "2"
                self.assertEqual(actual, result)












