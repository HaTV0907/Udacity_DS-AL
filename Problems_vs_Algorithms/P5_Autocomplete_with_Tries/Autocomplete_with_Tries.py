class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def _find_node(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

    def autocomplete(self, prefix = None):
        if None == prefix:
            return None
        if len(prefix) == 0:
            return -1
        node = self._find_node(prefix)
        suggestions = []
        if node:
            self._find_words(node, prefix, suggestions)
        return suggestions

    def _find_words(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self._find_words(child_node, prefix + char, suggestions)

# Example usage:
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.autocomplete("a"))  # Output: ['ant', 'anthology', 'antagonist', 'antonym']
print(MyTrie.autocomplete("f"))  # Output: ['fun', 'function', 'factory']
print(MyTrie.autocomplete("tr"))  # Output: ['trie', 'trigger', 'trigonometry', 'tripod']
print(MyTrie.autocomplete(""))  # Output: -1
print(MyTrie.autocomplete())  # Output: None
