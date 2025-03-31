import unittest
from collection.stack import stack

class TestStack(unittest.TestCase):
    def test_t0_get_length_of_stack(self):
        stack1 = stack()
        self.assertEqual(stack1.len(), second= 0)
        stack1.push(3)
        stack1.push(4)
        self.assertEqual(stack1.len(), second= 2)
    def test_element_can_add_stack(self):
        stack1 = stack()
        self.assertEqual(stack1.len(), second= 0)
        stack1.push(1)
        self.assertEqual(stack1.len(), second= 1)
        stack1.push(2)
        self.assertEqual(stack1.len(), second= 2)


    def test_element_can_pop_out_of_stack(self):
        stack2 = stack()
        stack2.push(1)
        stack2.push(2)
        stack2.pop()
        self.assertEqual(stack2.len(), second= 1)
        stack2.push(3)
        stack2.push(4)
        stack2.pop()
        self.assertEqual(stack2.len(), second= 2)

    def test_all_stacks_can_be_empty(self):
        stack1 = stack()
        self.assertEqual(stack1.len(), second= 0)
        stack1.push(3)
        stack1.push(4)
        stack1.clear()
        self.assertEqual(stack1.len(), second= 0)

    def test_that_stack_can_be_empty(self):
        stack1 = stack()
        self.assertEqual(stack1.isEmpty(), second= True)
        stack1.push(1)
        stack1.push(2)
        self.assertEqual(stack1.isEmpty(), second= False)

    def test_that_stack_can_remove_item(self):
        stack1 = stack()
        stack1.push(1)
        stack1.push(2)
        stack1.remove(2)
        self.assertEqual(stack1.len(), second= 1)
        stack1.remove(1)
        self.assertEqual(stack1.len(), second= 0)

    def test_that_stack_can_peek_element(self):
        stack1 = stack()
        stack1.push(1)
        stack1.push(2)
        stack1.push(3)
        self.assertEqual(stack1.peek(), 3)
        stack1.push(4)
        self.assertEqual(stack1.peek(), 4)



