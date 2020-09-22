from python_datastructures.linkedlist import SinglyLinkedList

# Stack implementation using a singly-linked-list.


class Stack:
    def __init__(self):
        self.__stack = SinglyLinkedList()

    def push(self, value):
        """Add element to the top of the stack.
        Args:
            Element (string,integer): add element to the top of the stack.
        """
        self.__stack.add(value)

    def pop(self):
        """Remove element from the top of the stack.

        Returns:
            Element: top of the stack.
        """
        self.__stack.remove()

    def peek(self):
        """View top element in the stack.

        Returns:
            Element: top of the stack.
        """
        return self.__stack.getHead()

    def isEmpty(self):
        """Check if stack is empty.

        Returns:
            boolean: True if no elements in the stack else False.
        """
        return True if self.__stack.getSize() == 0 else False

    def getSize(self):
        """Get size of the stack.

        Returns:
            integer: number of elements in the stack.
        """
        return self.__stack.getSize()

    def __str__(self):
        """Get string representation of the stack.

        Returns:
            Array: prints string representation of the stack.
        """
        return self.__stack.__str__()


if __name__ == "__main__":
    pass
