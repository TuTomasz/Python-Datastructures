# Node helper class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# Queue implementation using a doubly-linked-list.
class Queue:
    def __init__(self):
        self.__queue = Node(None)
        self.__head = self.__queue
        self.__tail = self.__queue
        self.__size = 0

    def getHead(self):
        """View first element in the queue.

        Returns:
            Element: first element in the queue.
        """
        if self.__size == 0:
            return None
        else:
            return self.__head.next.value

    def getTail(self):
        """View last element in the queue.

        Returns:
            Element: last element in the queue.
        """
        return self.__tail.value

    def dequeue(self):
        """Remove element from the queue.

        Returns:
            Element (any): remove element
        """
        nodeToRemove = self.__head.next
        if self.__size == 1:

            self.__tail = self.__queue
            self.__head = self.__queue
            self.__size -= 1
            return nodeToRemove.value

        else:
            self.__head.next = self.__head.next.next
            self.__size -= 1
            return nodeToRemove.value

    def enqueue(self, value):
        """Add element to queue.

        Args:
            Element (any): add element to the queue.
        """
        newNode = Node(value)
        newNode.previous = self.__tail
        self.__tail.next = newNode
        self.__tail = newNode
        self.__size += 1

    def getSize(self):
        """Get size of the queue.

        Returns:
            integer: number of elements in the queue.
        """
        return self.__size

    def isEmpty(self):
        """Check if queue is empty.

        Returns:
            boolean: True if no elements in the stack.
        """
        if self.__size > 0:
            return False
        return True

    def __str__(self):
        """Get string representation of the queue.

        Returns:
            String: prints string representation of the queue.
        """
        if not self.__queue.next:
            return str("Empty")
        else:
            result = []
            current = self.__queue.next
            while current:
                result.append(current.value)
                current = current.next
            return str(result)


if __name__ == "__main__":
    queue = Queue()
    
