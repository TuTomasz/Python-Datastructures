import unittest
from python_datastructures.dequeue import DeQueue


class Test_DeQueue(unittest.TestCase):
    def setUp(self):
        self.queue = DeQueue()

    def test_enqueue(self):
        self.queue.addFirst(2)
        self.assertEqual(self.queue.getSize(), 1)
        self.queue.addLast(3)
        self.assertEqual(self.queue.getSize(), 2)

    def test_dequeue_(self):
        self.queue.addFirst(3)
        self.assertEqual(self.queue.getSize(), 1)
        self.queue.pollFirst()
        self.assertEqual(self.queue.getSize(), 0)

    def test_isEmpty(self):
        self.assertEqual(self.queue.isEmpty(), True)
        self.queue.addLast(3)
        self.assertEqual(self.queue.isEmpty(), False)

    def test_getSize(self):
        self.assertEqual(self.queue.getSize(), 0)
        self.queue.addLast(3)
        self.assertEqual(self.queue.getSize(), 1)

    def test_get_tail(self):
        self.assertEqual(self.queue.getLast(), None)
        self.queue.addFirst(3)
        self.assertEqual(self.queue.getLast(), 3)

    def test_get_head(self):
        self.assertEqual(self.queue.getFirst(), None)
        self.queue.addLast(3)
        self.assertEqual(self.queue.getFirst(), 3)


if __name__ == "__main__":
    unittest.main()
