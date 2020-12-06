"""In computer science, a queue is a collection of entities that are maintained in a sequence and can be modified by the addition of entities at one end of the sequence and the removal of entities from the other end of the sequence."""

from python_datastructures.doublylinkedlist import DoublyLinkedList
from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self.__queue = DoublyLinkedList()

    def getHead(self) -> T:

        """View first element in the queue."""

        return self.__queue.getHead()

    def getTail(self):

        """View last element in the queue."""

        return self.__queue.getTail()

    def dequeue(self) -> T:

        """Remove element from the queue."""

        return self.__queue.removeAtHead()

    def enqueue(self, value: T) -> None:

        """Add element to queue."""

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
