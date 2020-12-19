import unittest
from python_datastructures import SinglyLinkedList


class Test_Queue(unittest.TestCase):
    def setUp(self):
        self.linkedlist = SinglyLinkedList()

    def test_add(self):
        self.linkedlist.add(2)
        self.assertEqual(self.linkedlist.getSize(), 1)
        self.assertEqual(self.linkedlist.getHead(), 2)

    def test_remove(self):
        self.linkedlist.add(2)
        self.linkedlist.add(3)
        self.linkedlist.add(4)
        self.assertEqual(self.linkedlist.getSize(), 3)
        self.linkedlist.remove()
        self.assertEqual(self.linkedlist.getSize(), 2)
        self.linkedlist.remove()
        self.assertEqual(self.linkedlist.getSize(), 1)
        self.linkedlist.remove()
        self.assertEqual(self.linkedlist.getSize(), 0)
        self.assertEqual(self.linkedlist.remove(), None)

    def test_isEmpty(self):
        self.assertEqual(self.linkedlist.isEmpty(), True)
        self.linkedlist.add(3)
        self.assertEqual(self.linkedlist.isEmpty(), False)

    def test_getSize(self):
        self.assertEqual(self.linkedlist.getSize(), 0)
        self.linkedlist.add(3)
        self.assertEqual(self.linkedlist.getSize(), 1)

    def test_get_head(self):
        self.assertEqual(self.linkedlist.getHead(), None)
        self.linkedlist.add(4)
        self.assertEqual(self.linkedlist.getHead(), 4)

    def test_toArray(self):
        self.linkedlist.add(3)
        self.linkedlist.add(4)
        self.assertEqual(self.linkedlist.__str__(), "[4, 3]")


if __name__ == "__main__":
    unittest.main()
