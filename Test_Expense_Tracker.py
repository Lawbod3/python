import unittest
import Expenses

class TestPrintMenuFunction(unittest.TestCase):

      def test_that_print_menu_exist(self):
               Expenses.print_menu()

      def test_that_print__menu_correct_value(self):
               actual = Expenses.print_menu()
               result = """
    Welcome to Semicolon Expense Tracker App
    —------------------------------------------
    1. Add an expense
    2. View all expenses
    3. Calculate total expenses
    4. Exit

"""

               self.assertEqual(actual, result)


class TestValidateFunction(unittest.TestCase):

      def test_that_validate_date_exist(self):
                Expenses.validate_date("2/12/2020")

      def test_that_validate_date_correct_value(self):
               actual = Expenses.validate_date("2/12/2020")
               result = True
               self.assertEqual(actual, result)

class TestValidateDescriptionFunction(unittest.TestCase):
      
      def test_that_validate_description_exist(self):
               Expenses.validate_description(" hello")

      def test_that_validate_description_correct_value(self):
               actual = Expenses.validate_description(" hello")
               result = True
               self.assertEqual(actual, result)
      
class TestValidateAmountFunction(unittest.TestCase):

      def test_that_validate_amount_exist(self):
               Expenses.validate_amount(-5)

      def test_that_validate_amount_correct_value(self):
               actual = Expenses.validate_amount(-5)
               result = False
               self.assertEqual(actual, result)

class TestTotalAmountFunction(unittest.TestCase):
      
       def test_that_total_amount_exist(self):
               value = (2, 2, 2, 4, 2)
               Expenses.total_amount(value)
      
       def test_that_total_amount_correct_value(self):
               value = (2, 2, 2, 4, 2)
               actual = Expenses.total_amount(value)
               result = 12
               self.assertEqual(actual, result)


               










