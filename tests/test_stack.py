import unittest
from python_datastructures.stack import Stack

class Test_Stack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(2)
        self.assertEqual(self.stack.getSize(),1)
    
    def test_pop(self):
        self.stack.push(2)
        self.assertEqual(self.stack.getSize(),1)
        self.stack.pop()
        self.assertEqual(self.stack.getSize(),0)

    def test_isEmpty(self):
        self.assertEqual(self.stack.isEmpty(),True)
        self.stack.push(3)
        self.assertEqual(self.stack.isEmpty(),False)

    def test_getSize(self):
        self.assertEqual(self.stack.getSize(),0)
        self.stack.push(3)
        self.assertEqual(self.stack.getSize(),1)

    def test_peek(self):
        self.assertEqual(self.stack.peek(),None)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(),3)

if __name__ == "__main__":
    unittest.main()


