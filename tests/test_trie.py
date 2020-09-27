import unittest
from python_datastructures.trie import Trie


class Test_Trie(unittest.TestCase):
    def setUp(self):
        words = ["apple", "app", "android", "and"]
        self.trie = Trie()
        self.trie.build(words)

    def test_add(self):

        self.trie.add("amazon")
        self.assertEqual(self.trie.wordcount, 5)

    def test_contains(self):

        self.assertEqual(self.trie.contains("app"), True)
        self.assertEqual(self.trie.contains("amazon"), False)
        self.assertEqual(self.trie.contains("ap"), True)


if __name__ == "__main__":
    unittest.main()
