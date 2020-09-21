import unittest
from python_datastructures.doublylinkedlist import DoublyLinkedList

class Test_Queue(unittest.TestCase):

    def setUp(self):
        self.linkedlist = DoublyLinkedList()

    def test_isEmpty(self):
        self.assertEqual(self.linkedlist.isEmpty(),True)
        self.linkedlist.addAtHead(3)
        self.assertEqual(self.linkedlist.isEmpty(),False)

    def test_getSize(self):
        self.assertEqual(self.linkedlist.getSize(),0)
        self.linkedlist.addAtTail(3)
        self.assertEqual(self.linkedlist.getSize(),1)

    def test_get_head(self):
        self.assertEqual(self.linkedlist.getHead(),None)
        self.linkedlist.addAtTail(4)
        self.assertEqual(self.linkedlist.getHead(),4)

    def test_get_tail(self):
        self.assertEqual(self.linkedlist.getTail(),None)
        self.linkedlist.addAtHead(4)
        self.assertEqual(self.linkedlist.getTail(),4)

    def test_insert_at_head(self):
        # when list empty
        self.linkedlist.addAtHead(5)
        self.assertEqual(self.linkedlist.__str__(), '[5]')
        # when list 1 element
        self.linkedlist.addAtHead(4)
        self.assertEqual(self.linkedlist.__str__(), '[4, 5]')
        # when list more then 1 element
        self.linkedlist.addAtHead(3)
        self.assertEqual(self.linkedlist.__str__(), '[3, 4, 5]')

    def test_insert_at_tail(self):
        # when list empty
        self.linkedlist.addAtTail(5)
        self.assertEqual(self.linkedlist.__str__(), '[5]')
        # when list 1 element
        self.linkedlist.addAtTail(4)
        self.assertEqual(self.linkedlist.__str__(), '[5, 4]')
        # when list more then 1 element
        self.linkedlist.addAtTail(3)
        self.assertEqual(self.linkedlist.__str__(), '[5, 4, 3]')

    def test_remove_at_head(self):

        # if list empty
        self.assertEqual(self.linkedlist.removeAtHead(),None)

        # if list has 1 element
        self.linkedlist.addAtHead(1)
        self.linkedlist.removeAtHead()
        self.assertEqual(self.linkedlist.__str__(),'[]')
        
        # if list multiple elements
        self.linkedlist.addAtHead(1)
        self.linkedlist.addAtHead(2)
        self.linkedlist.addAtHead(3)
        self.linkedlist.removeAtHead()
        self.assertEqual(self.linkedlist.__str__(),'[2, 1]')
    
    def test_remove_at_tail(self):

        # if list empty
        self.assertEqual(self.linkedlist.removeAtTail(),None)

        # if list has 1 element
        self.linkedlist.addAtHead(1)
        self.linkedlist.removeAtTail()
        self.assertEqual(self.linkedlist.__str__(),'[]')

        # if list multiple elements
        self.linkedlist.addAtHead(1)
        self.linkedlist.addAtHead(2)
        self.linkedlist.addAtHead(3)
        self.linkedlist.removeAtTail()
        self.assertEqual(self.linkedlist.__str__(),'[3, 2]')

    
if __name__ == "__main__":
    unittest.main()


