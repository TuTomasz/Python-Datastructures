
from .queue import Queue 
from .stack import Stack

class Node:

    # constructor
    def __init__(self, data,left=None,right=None):
       self.data = data
       self.left = left
       self.right = right

class BinaryTree:

    # constructor
    def __init__(self):
        self.root = None

    # add element to the binary tree
    # best o(h) worst o(n)
    def insert(self,data):

        if self.root is None:
            self.root = Node(data)
        elif self.contains(data):
            return "element already exists"
        else:
            self.__add(data,self.root)

    # helper method recursively traverses and adds element to the tree
    # in the right position
    def __add(self,data,node):

        if data < node.data:
            if node.left is not None:
                self.__add(data,node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self.__add(data,node.right)
            else:
                node.right = Node(data)

    # print the content of the tree using various traversal methoods
    def printTree(self,root,traversalType):
        traversal = ""

        if traversalType == "preorder":
            traversal = self.preOrder(root,traversal)
        elif traversalType == "inorder":
            traversal = self.inOrder(root,traversal)
        elif traversalType == "postorder":
            traversal = self.postOrder(root,traversal)
        elif traversalType == "levelorder":
            traversal = self.levelOrder(root,traversal)
        elif traversalType == "reverseorder":
            traversal = self.reverseLevelOrder(root,traversal)
        else:
            print("unknown input")

        return traversal

    # pre order traversal
    def preOrder(self,root,traversal):

        if root:
            traversal += (str(root.data) + " ")
            traversal = self.preOrder(root.left,traversal)
            traversal = self.preOrder(root.right,traversal)
        return traversal

    # in order traversal
    def inOrder(self,root,traversal):

        if root:

            traversal = self.inOrder(root.left,traversal)
            traversal += (str(root.data) + " ")
            traversal = self.inOrder(root.right,traversal)

        return traversal

    # post order traversal
    def postOrder(self,root,traversal):

        if root:

            traversal = self.postOrder(root.left,traversal)
            traversal = self.postOrder(root.right,traversal)
            traversal += (str(root.data) + " ")

        return traversal

    # bfs
    def levelOrder(self,root,traversal):

        queue = Queue()
        queue.enqueue(root)
    
        while not queue.isEmpty():

            node = queue.dequeue()
            traversal += str(node.data) + " "

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    # reverse level order traversal
    def reverseLevelOrder(self,root,traversal):

        queue = Queue()
        stack = Stack()
        queue.enqueue(root)

        while not queue.isEmpty():

            node = queue.dequeue()
            stack.push(node)

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        while not stack.isEmpty():

            node = stack.pop()
            traversal += str(node.data) + " "
            
        return traversal

    # calculate the height of the tree
    # o(n)
    def getheight(self,root):

        return self.__height(self.root)

    # helper methood that runs recursively to calculate the height of the tree
    # starting at the tree root
   
    def __height(self,root):

        if root is None:
            return -1
        
        left = self.__height(root.left)
        right = self.__height(root.right)

        return 1 + max(left, right)

    # calculate the size of the tree 
    # o(n)
    def getSize(self):

        return self.__size(self.root)

    # helper methood that runs recursively to calculate the size of the tree
    # starting at the tree root
    def __size(self,root):

        if root is None:
            return 0
        
        left = self.__size(root.left)
        right = self.__size(root.right)

        return 1 + left + right

    # check if element exist in the tree
    # best log(n) worst o(n)
    def contains(self,data):

        return self.__contains(self.root,data)

    # recursive helper method
    def __contains(self,node,data):

        if node is None:
            return False
        if data < node.data:
            return self.__contains(node.left,data)
        if data > node.data:
            return self.__contains(node.right,data)
        else:
            return True

    # checks if a tree is a BST tree
    # o(n)
    def isBst(self):

        return self.__isBst(self.root,min=float('-inf'), max =float('inf'))

    def __isBst(self, node, min ,max):

        if node is None:
            return True
        if (node.data < min or node.data > max ):
            return False
        
        return self.__isBst(node.left,min, node.data) and self.__isBst(node.right,node.data,max)
        
    

        