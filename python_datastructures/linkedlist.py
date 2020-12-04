from typing import TypeVar


T = TypeVar("T")

# Node helper class
class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None


# Implementation of SinglyLinkedList


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
