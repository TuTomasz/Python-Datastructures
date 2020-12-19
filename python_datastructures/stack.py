"""Stack is an abstract data type that serves as a collection of elements, with two main principal operations: Push, which adds an element to the collection, and Pop, which removes the most recently added element that was not yet removed."""

from python_datastructures.linkedlist import SinglyLinkedList
from typing import TypeVar


T = TypeVar("T")


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

        return str(self.__stack.toArray()[::-1])


if __name__ == "__main__":
    pass
