"""In computer science, a double-ended queue is an abstract data type that generalizes a queue, for which elements can be added to or removed from either the front or back. It is also often called a head-tail linked list, though properly this refers to a specific data structure implementation of a deque."""

from python_datastructures.doublylinkedlist import DoublyLinkedList
from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None
        self.previous = None


class DeQueue:
    def __init__(self):
        self.__queue = DoublyLinkedList()

    def getFirst(self) -> T:

        """View first element in the dequeue."""

        return self.__queue.getHead()

    def getLast(self):

        """View last element in the dequeue."""

        return self.__queue.getTail()

    def pollFirst(self) -> T:

        """Remove element from the queue at head."""

        return self.__queue.removeAtHead()

    def pollLast(self) -> T:

        """Remove element from the queue at tail."""

        return self.__queue.removeAtTail()

    def addFirst(self, value: T) -> None:

        """Add element to dequeue at head end"""

        self.__queue.addAtHead(value)

    def addLast(self, value: T) -> None:

        """Add element to dequeue at tail end"""

        self.__queue.addAtTail(value)

    def getSize(self) -> int:

        """Get size of the queue."""

        return self.__queue.getSize()

    def isEmpty(self) -> bool:

        """Check if queue is empty."""

        return self.__queue.isEmpty()

    def __str__(self) -> str:

        """Get string representation of the queue."""

        return self.__queue.__str__()


if __name__ == "__main__":
    pass
