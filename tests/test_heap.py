import unittest
from python_datastructures.heap import MinHeap
from python_datastructures.heap import MaxHeap

class Test_Min_Heap(unittest.TestCase):
    def setUp(self):
        array = [2,3,1,5,9,5,4,7]
        self.heap = MinHeap(array)
    
    def test_peek(self):
        self.assertEqual(self.heap.peek(),1)

    def test_add(self):
        self.heap.add(-1)
        self.assertEqual(self.heap.peek(),-1)

    def test_remove(self):
        removed = self.heap.remove()
        self.assertEqual(removed,1)
        self.assertEqual(self.heap.peek(),2)
        self.assertEqual(len(self.heap.heap),7)

class Test_Max_Heap(unittest.TestCase):
    def setUp(self):
        array = [2,3,1,5,9,5,4,7]
        self.heap = MaxHeap(array)
    
    def test_peek(self):
        self.assertEqual(self.heap.peek(),9)

    def test_add(self):
        self.heap.add(10)
        self.assertEqual(self.heap.peek(),10)

    def test_remove(self):
        removed = self.heap.remove()
        self.assertEqual(removed,9)
        self.assertEqual(self.heap.peek(),7)
        self.assertEqual(len(self.heap.heap),7)

if __name__ == "__main__":
    unittest.main()