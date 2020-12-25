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

    def add(self, value: T):
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

    def minValueNode(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def remove(self, value):

        if self.contains(value):
            if self.size == 1:
                self.root = None
                self.size -= 1

            else:
                self.__remove(self.root, value)
                self.size -= 1
        else:
            pass

    def __remove(self, root, value: T):
        def minValueNode(node):
            current = node

            while current.left is not None:
                current = current.left

            return current

        if root is None:
            return root

        if value < root.value:
            root.left = self.__remove(root.left, value)

        elif value > root.value:
            root.right = self.__remove(root.right, value)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = minValueNode(root.right)

            root.value = temp.value

            root.right = self.__remove(root.right, temp.value)

        return root

    def isValid(self):
        pass

    def build(self, array: list) -> None:

        self.root = self.__build(array, None, 0, len(array) - 1)

    def __build(self, array: list, root, left: int, right: int):

        if left > right:
            return

        mid = (left + right) // 2

        if not root:

            root = Node(array[mid])
            self.size += 1

        else:

            self.__add(root, array[mid])

        self.__build(array, root, left, mid - 1)
        self.__build(array, root, mid + 1, right)

        return root

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
    tree2.build([1, 2, 3])
    print(tree2, tree2.size)
    tree2.remove(1)
    print(tree2, tree2.size)
    tree2.remove(3)
    print(tree2, tree2.size)
    tree2.remove(2)
    print(tree2, tree2.size)
