from python_datastructures.linkedlist import SinglyLinkedList
from typing import TypeVar


T = TypeVar("T")

# Stack implementation using a singly-linked-list.
class Stack:
    def __init__(self):
        self.__stack = SinglyLinkedList()

    def push(self, value: T) -> None:

        """Add element to the top of the stack."""

        self.__stack.add(value)

    def pop(self) -> T:

        """Remove element from the top of the stack."""

        return self.__stack.remove()

    def peek(self) -> T:

        """View top element in the stack."""

        return self.__stack.getHead()

    def isEmpty(self) -> bool:

        """Check if stack is empty."""

        return True if self.__stack.getSize() == 0 else False

    def getSize(self) -> int:

        """Get size of the stack."""

        return self.__stack.getSize()

    def __str__(self) -> str:

        """Get string representation of the stack."""

        return self.__stack.__str__()


if __name__ == "__main__":
    pass
