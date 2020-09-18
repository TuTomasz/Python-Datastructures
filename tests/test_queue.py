import unittest
from python_datastructures.queue import Queue

class Test_Queue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(2)
        self.assertEqual(self.queue.getSize(),1)
    
    def test_dequeue(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.getSize(),1)
        self.queue.dequeue()
        self.assertEqual(self.queue.getSize(),0)

    def test_isEmpty(self):
        self.assertEqual(self.queue.isEmpty(),True)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.isEmpty(),False)

    def test_getSize(self):
        self.assertEqual(self.queue.getSize(),0)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.getSize(),1)

    def test_get_tail(self):
        self.assertEqual(self.queue.getTail(),None)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.getTail(),3)

    def test_get_head(self):
        self.assertEqual(self.queue.getHead(),None)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.getHead(),3)

if __name__ == "__main__":
    unittest.main()


