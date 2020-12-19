"""Linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. """

from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.__sentinel = Node(None)
        self.__head = self.__sentinel
        self.__size = 0

    def add(self, value: T) -> None:

        """Add element to linked list."""

        newNode = Node(value)
        if self.__size == 0:
            self.__head.next = newNode
            self.__head = newNode
            self.__size += 1
        else:
            self.__sentinel.next = newNode
            newNode.next = self.__head
            self.__head = newNode
            self.__size += 1

    def remove(self):

        """Remove node from linkedlist."""

        if self.__size == 0:
            return None
        if self.__size >= 1:
            nodeToRemove = self.__head
            self.__sentinel.next = None
            self.__head = self.__sentinel
            self.__size -= 1
            return nodeToRemove
        else:
            nodeToRemove = self.__head
            self.__sentinel.next = self.__head.next
            self.__head = self.__sentinel.next
            self.__size -= 1
            return nodeToRemove

    def getHead(self) -> T:

        """Get value of the linkedlist head node."""

        return self.__head.value

    def getHeadNode(self) -> Node:

        """Get head node referance."""

        return self.__head

    def getSize(self) -> int:

        """Return size of the linkedlist."""

        return self.__size

    def isEmpty(self) -> bool:

        """Checks if linkedlist is empty."""

        return True if self.__size == 0 else False

    def toArray(self) -> list:

        """Converts linkedlist to list."""

        arr = []
        current = self.__head
        while current:
            arr.append(current.value)
            current = current.next
        return arr

    def __str__(self) -> str:

        """Return String representation of linkedlist values."""

        arr = []
        current = self.__head
        while current:
            arr.append(current.value)
            current = current.next
        return str(arr)


if __name__ == "__main__":
    pass
