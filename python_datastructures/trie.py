"""Trie, also called digital tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings."""

from typing import TypeVar


T = TypeVar("T")


class Trie:
    # Static variables
    wordcount = 0

    def __init__(self):
        self.__root = {}
        self.__end = ""

    def build(self, array: list) -> None:

        """Builds a trie structure given array of words"""

        for el in array:
            self.add(el)

    def add(self, string: str) -> None:

        """Add word to the trie structure"""

        self.wordcount += 1
        node = self.__root
        for i in range(len(string)):
            char = string[i]
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.__end] = "*"

    def contains(self, string: str) -> bool:

        """Checks if a trie contains a word or substring of word"""

        node = self.__root
        for i in range(len(string)):
            char = string[i]
            if char not in node:
                return False
            else:
                node = node[char]
        return True


if __name__ == "__main__":
    pass
