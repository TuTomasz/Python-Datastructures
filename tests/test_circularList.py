import unittest
from python_datastructures import CircularList


class Test_Queue(unittest.TestCase):
    def setUp(self):
        self.circularList = CircularList()

    def test_isEmpty(self):
        self.assertEqual(self.circularList.isEmpty(), True)
        self.circularList.add(3)
        self.assertEqual(self.circularList.isEmpty(), False)

    def test_getSize(self):
        self.assertEqual(self.circularList.getSize(), 0)
        self.circularList.add(3)
        self.assertEqual(self.circularList.getSize(), 1)

    def test_add(self):
        # when list empty
        self.circularList.add(5)
        self.assertEqual(self.circularList.__str__(), "[5]")
        # when list 1 element
        self.circularList.add(4)
        self.assertEqual(self.circularList.__str__(), "[5, 4]")
        # when list more then 1 element
        self.circularList.add(3)
        self.assertEqual(self.circularList.__str__(), "[5, 4, 3]")

    def test_remove(self):

        # if list empty
        self.assertEqual(self.circularList.remove(), None)

        # if list has 1 element
        self.circularList.add(1)
        self.circularList.remove()
        self.assertEqual(self.circularList.__str__(), "[]")

        # if list multiple elements
        self.circularList.add(1)
        self.circularList.add(2)
        self.circularList.add(3)
        self.circularList.remove()
        self.assertEqual(self.circularList.__str__(), "[2, 3]")

    def test_getTailValue(self):

        # when list empty
        self.assertEqual(self.circularList.getTailValue(), None)

        # if list has 1 element
        self.circularList.add(5)
        self.assertEqual(self.circularList.getTailValue(), 5)

        # if list multiple elements
        self.circularList.add(1)
        self.circularList.add(2)
        self.circularList.add(3)
        self.assertEqual(self.circularList.getTailValue(), 3)

    def test_getHeadValue(self):

        # when list empty
        self.assertEqual(self.circularList.getHeadValue(), None)

        # if list has 1 element
        self.circularList.add(5)
        self.assertEqual(self.circularList.getHeadValue(), 5)

        # if list multiple elements
        self.circularList.add(1)
        self.circularList.add(2)
        self.circularList.add(3)
        self.assertEqual(self.circularList.getHeadValue(), 5)

    def test_getCurrent(self):

        # when list empty
        self.assertEqual(self.circularList.getCurrent(), None)

        # if list has 1 element
        self.circularList.add(5)
        self.assertEqual(self.circularList.getCurrent(), None)

        # if list multiple elements
        self.circularList.add(1)
        self.circularList.add(2)
        self.circularList.add(3)
        self.assertEqual(self.circularList.getCurrent(), None)

        # when we itterate towards forward getNext()
        self.circularList.getNext()
        self.assertEqual(self.circularList.getCurrent(), 5)

        # when we itterate towards the back getPrev()
        self.circularList.getPrevious()
        self.assertEqual(self.circularList.getCurrent(), 3)

    def test_getNext(self):
        pass

    def test_getPrevious(self):
        pass


if __name__ == "__main__":
    unittest.main()
