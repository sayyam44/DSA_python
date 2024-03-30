class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Initialize children as a list of 26 elements
        self.flag = False

class Solution:
    def __init__(self):
        self.root = TrieNode()  # Create an instance of TrieNode

    def add(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()  # Create a new TrieNode if necessary
            curr = curr.children[index]
        curr.flag = True

    def search(self, word):
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children:
                        if child is not None and dfs(i + 1, child):
                            return True
                    return False  # No matching child found for '.'
                else:
                    index = ord(c) - ord('a')
                    if curr.children[index] is None:
                        return False  # Character not found in Trie
                    curr = curr.children[index]
            return curr.flag

        return dfs(0, self.root)


# Example usage:
trie = Solution()
trie.add("apple")
trie.add("application")
trie.add("banana")

print(trie.search("app"))  # Output: True
print(trie.search("ap."))  # Output: True (Matches "apple")
print(trie.search("b.nana"))  # Output: True (Matches "banana")
print(trie.search("b..ana"))  # Output: False (No match in Trie)
print(trie.search("appl."))  # Output: False (No match in Trie)
