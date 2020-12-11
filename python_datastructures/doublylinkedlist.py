"""Doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains three fields: two link fields and one data field."""

from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.__sentinel = Node(None)
        self.__head = self.__sentinel
        self.__tail = self.__sentinel
        self.__size = 0

    def addAtHead(self, value: T) -> None:

        """Add node at head end."""

        if self.__size == 0:
            newNode = Node(value)
            self.__sentinel.next = newNode
            newNode.prev = self.__sentinel
            self.__tail = newNode
            self.__size += 1
        else:
            newNode = Node(value)
            nextNode = self.__sentinel.next
            self.__sentinel.next = newNode
            newNode.prev = self.__sentinel
            newNode.next = nextNode
            nextNode.prev = newNode
            self.__size += 1

    def addAtTail(self, value: T) -> None:

        """Add node at tail end."""

        if self.__size == 0:
            newNode = Node(value)
            self.__sentinel.next = newNode
            newNode.prev = self.__sentinel
            self.__tail = newNode
            self.__size += 1
        else:
            newNode = Node(value)
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
            self.__size += 1

    def removeAtHead(self):

        """Remove node at head end."""

        if self.__size == 0:
            return None
        elif self.__size == 1:
            nodeToRemove = self.__head.next
            self.__sentinel.next = None
            nodeToRemove.prev = None
            self.__size -= 1
            return nodeToRemove
        else:
            nodeToRemove = self.__head.next
            nextNode = nodeToRemove.next
            self.__sentinel.next = nextNode
            nextNode.prev = self.__sentinel
            nodeToRemove.next = None
            nodeToRemove.prev = None
            self.__size -= 1
            return nodeToRemove

    def removeAtTail(self):

        """Remove node at tail end."""

        if self.__size == 0:
            return None
        elif self.__size == 1:
            nodeToRemove = self.__tail
            nodeToRemove.prev = None
            self.__sentinel.next = None
            self.__head = self.__sentinel
            self.__tail = self.__sentinel
            self.__size -= 1
            return nodeToRemove
        else:
            nodeToRemove = self.__tail
            previous = nodeToRemove.prev
            nodeToRemove.prev = None
            previous.next = None
            self.__tail = previous
            self.__size -= 1
            return nodeToRemove

    def isEmpty(self) -> bool:

        """Check if linkedlist is empty"""

        return True if self.__size == 0 else False

    def getHead(self):

        """Get value at the front end of the list."""

        if self.__size == 0:
            return None
        else:
            return self.__head.next.value

    def getTail(self) -> T:

        """Get value at the tail of the list."""

        return self.__tail.value

    def getSize(self) -> int:

        """Get length of the linked list."""

        return self.__size

    def __len__(self) -> int:

        """Get length of the linked list."""

        return self.__size

    def __str__(self) -> str:

        """Return String representation of linkedlist values."""

        arr = []
        current = self.__head.next
        while current:
            arr.append(current.value)
            current = current.next
        return str(arr)


if __name__ == "__main__":
    pass
