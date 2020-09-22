class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.__sentinel = Node(None)
        self.__head = self.__sentinel
        self.__tail = self.__sentinel
        self.__size = 0

    def addAtHead(self, value):
        """Add node at head end.

        Args:
            value (Any): value to be added.
        """
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

    def addAtTail(self, value):
        """Add node at tail end.

        Args:
            value (Any): value to be added.
        """
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
        """Remove node at head end.

        Returns:
            Any: returns value of the node.
        """
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
        """Remove node at tail end.

        Returns:
            Any: returns value of the node.
        """
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

    def isEmpty(self):
        """Check if linkedlist is empty

        Returns:
            Boolean: True if list empty else False
        """
        return True if self.__size == 0 else False

    def getHead(self):
        """Get value at the front end of the list.

        Returns:
            Any: value at the tail end of the list.
        """
        if self.__size == 0:
            return None
        else:
            return self.__head.next.value

    def getTail(self):
        """Get value at the tail of the list.

        Returns:
            Any: value at the tail end of the list.
        """
        return self.__tail.value

    def getSize(self):
        """Get length of the linked list.

        Returns:
            Integer: Size of the doubly linkedlist.
        """
        return self.__size

    def __len__(self):
        """Get length of the linked list.

        Returns:
            Integer: Size of the doubly linkedlist.
        """
        return self.__size

    def __str__(self):
        """Return String representation of linkedlist values.

        Returns:
            String: String representation of linkedlist.
        """
        arr = []
        current = self.__head.next
        while current:
            arr.append(current.value)
            current = current.next
        return str(arr)


if __name__ == "__main__":
    pass
