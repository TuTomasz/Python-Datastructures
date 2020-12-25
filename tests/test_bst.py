import unittest
from python_datastructures import BST


class Test_Queue(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.bst.add(5)
        self.bst.add(4)
        self.bst.add(1)

    def test_add(self):

        # add when does not exist
        self.assertEqual(self.bst.root.right, None)
        self.assertEqual(self.bst.size, 3)
        self.bst.add(6)
        self.assertEqual(self.bst.root.right.value, 6)
        self.assertEqual(self.bst.size, 4)

        # add a duplicate
        self.assertEqual(self.bst.root.left.value, 4)
        self.assertEqual(self.bst.size, 4)
        self.bst.add(4)
        self.assertEqual(self.bst.root.left.value, 4)
        self.assertEqual(self.bst.size, 4)

    def test_contains(self):
        pass

    def test_build(self):

        newTree = BST()
        newTree.build([1, 2, 3, 4, 5, 6, 7, 8])

        inOrder = newTree.getOrder("inOrder")
        preOrder = newTree.getOrder("preOrder")
        postOrder = newTree.getOrder("postOrder")

        # test if the order of the tree matches up with various traversal options
        self.assertEqual(inOrder, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(preOrder, [4, 2, 1, 3, 6, 5, 7, 8])
        self.assertEqual(postOrder, [2, 1, 3, 6, 5, 7, 8, 4])

    def test_delete(self):
        pass

    def test_isValid(self):
        pass

    def test_getOrder(self):

        inOrder = self.bst.getOrder("inOrder")
        preOrder = self.bst.getOrder("preOrder")
        postOrder = self.bst.getOrder("postOrder")

        self.assertEqual(inOrder, [1, 4, 5])
        self.assertEqual(preOrder, [5, 4, 1])
        self.assertEqual(postOrder, [4, 1, 5])


if __name__ == "__main__":
    unittest.main()
