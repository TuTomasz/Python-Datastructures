"""Binary search tree, also called an ordered or sorted binary tree (BST), is a rooted binary tree whose internal nodes each store a key greater than all the keys in the node's left subtree and less than those in its right subtree."""

from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        if self.contains(value):
            return False
        elif self.root == None:
            self.root = Node(value)
            self.size += 1
        else:
            self.__add(self.root, value)

    def __add(self, root, value):
        if value < root.value:
            if root.left == None:
                root.left = Node(value)
                self.size += 1
            else:
                self.__add(root.left, value)
        elif value >= root.value:
            if root.right == None:
                root.right = Node(value)
                self.size += 1
            else:
                self.__add(root.right, value)

    def contains(self, value):

        return self.__contains(self.root, value)

    def __contains(self, root, value):
        if root == None:
            return False
        elif root.value == value:
            return True
        else:
            if value < root.value:
                return self.__contains(root.left, value)
            else:
                return self.__contains(root.right, value)

    def remove(self, value):
        pass

    def isValid(self):
        pass

    def build(self, array):

        self.root = self.__build(array, self.root, 0, len(array) - 1)

    def __build(self, array, root, left, right):

        if left > right:
            return

        mid = (left + right) // 2

        if not root:

            root = Node(array[mid])
        else:

            self.add(array[mid])

        self.__build(array, root, left, mid - 1)
        self.__build(array, root, mid + 1, right)

        return self.root

    def getOrder(self, order="inOrder"):
        def inOrder(root):
            if root:
                inOrder(root.left)
                traversal.append(root.value)
                inOrder(root.right)

        def preOrder(root):
            if root:
                traversal.append(root.value)
                preOrder(root.left)
                preOrder(root.right)

        def postOrder(root):
            if root:
                preOrder(root.left)
                preOrder(root.right)
                traversal.append(root.value)

        traversal = []
        if order == "inOrder":
            inOrder(self.root)
            return traversal
        elif order == "preOrder":
            preOrder(self.root)
            return traversal
        elif order == "postOrder":
            postOrder(self.root)
            return traversal

    def __len__(self):
        return self.size

    def __str__(self):
        """Return String representation of BST values.

        Returns:
            String: String inorder representaion of BST.
        """

        return str(self.getOrder())


if __name__ == "__main__":

    tree = BST()

    tree.add(3)
    tree.add(2)
    tree.add(4)

    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)

    tree2 = BST()
    tree2.build([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(tree2.getOrder("preOrder"))
    print(tree2)
    print(len(tree2))
