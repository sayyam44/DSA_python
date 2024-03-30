class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Assuming lowercase English alphabet
        self.flag = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                curr.children[i] = TrieNode()  # Create a new TrieNode if necessary
            curr = curr.children[i]
        curr.flag = True  # Mark the end of the word in the trie

    def search(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return curr.flag  # Check if the word exists and ends at a valid node

    def starts_with(self, prefix):
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return True  # Return True if the prefix exists in the trie

# Example usage:
trie = Trie()
words = ["apple", "app", "application", "banana", "bat", "cat"]

for word in words:
    trie.insert(word)

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("application"))  # Output: True
print(trie.search("appl"))   # Output: False (Partial word not inserted)
print(trie.search("banana")) # Output: True
print(trie.search("bat"))    # Output: True
print(trie.search("cat"))    # Output: True
print(trie.search("dog"))    # Output: False

print(trie.starts_with("app"),"heyyyyyyyyy")  # Output: True
print(trie.starts_with("ban"))  # Output: False (No word starts with "ban")
print(trie.starts_with("c"))    # Output: True (Prefix exists in "cat")
print(trie.starts_with("d"))    # Output: False (No word starts with "d")

