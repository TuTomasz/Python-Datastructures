
# Node helper class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Implementation of SinglyLinkedList


class SinglyLinkedList():
    def __init__(self):
        self.__sentinel = Node(None)
        self.__head = self.__sentinel
        self.__size = 0

    def add(self, value):
        """Add element to linked list.

        Args:
            value (Any): value to be added.
        """
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
        """ Remove node from linkedlist.

        Returns:
            Any: returns value of the node.
        """
        if self.__size == 0:
            return None
        elif self.__size == 1:
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

    def getHead(self):
        """Get value of the linkedlist head node.

        Returns:
            Any: value of the head of the linkedlist.
        """
        return self.__head.value

    def getSize(self):
        """Return size of the linkedlist.

        Returns:
            Integer: number of nodes in the linkedlist.
        """
        return self.__size

    def isEmpty(self):
        """Checks if linkedlist is empty.

        Returns:
            Boolean: Return True if linkedlist is empty else False.
        """
        return True if self.__size == 0 else False

    def __str__(self):
        """Return String representation of linkedlist values.

        Returns:
            String: String representation of linkedlist.
        """
        arr = []
        current = self.__head
        while current:
            arr.append(current.value)
            current = current.next
        return str(arr)


if __name__ == "__main__":
    pass
