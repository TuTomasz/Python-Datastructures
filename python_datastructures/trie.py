class Trie:
    # Static variables
    wordcount = 0

    def __init__(self):
        self.__root = {}
        self.__end = ""

    def build(self, array):
        """Builds a trie structure given array of words

        Args:
            array ([string]): array of words
        """
        for el in array:
            self.add(el)

    def add(self, string):
        """Add word to the trie structure

        Args:
            string (string): add word to the trie structure
        """
        self.wordcount += 1
        node = self.__root
        for i in range(len(string)):
            char = string[i]
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.__end] = '*'

    def contains(self, string):
        """Checks if a trie contains a word or substring of word

        Args:
            string (string): word to be searched

        Returns:
            boolean: True if word present else False
        """

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
