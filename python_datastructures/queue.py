from python_datastructures.doublylinkedlist import DoublyLinkedList

# Node helper class


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# Queue implementation using a doubly-linked-list.


class Queue:
    def __init__(self):
        self.__queue = DoublyLinkedList()

    def getHead(self):
        """View first element in the queue.

        Returns:
            Element: first element in the queue.
        """
        return self.__queue.getHead()

    def getTail(self):
        """View last element in the queue.

        Returns:
            Element: last element in the queue.
        """
        return self.__queue.getTail()

    def dequeue(self):
        """Remove element from the queue.

        Returns:
            Element (any): remove element
        """
        return self.__queue.removeAtHead()

    def enqueue(self, value):
        """Add element to queue.

        Args:
            Element (any): add element to the queue.
        """
        self.__queue.addAtTail(value)

    def getSize(self):
        """Get size of the queue.

        Returns:
            integer: number of elements in the queue.
        """
        return self.__queue.getSize()

    def isEmpty(self):
        """Check if queue is empty.

        Returns:
            boolean: True if no elements in the stack.
        """
        return self.__queue.isEmpty()

    def __str__(self):
        """Get string representation of the queue.

        Returns:
            String: prints string representation of the queue.
        """
        return self.__queue.__str__()


if __name__ == "__main__":
    pass
