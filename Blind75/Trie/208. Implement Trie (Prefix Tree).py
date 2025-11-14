class TrieNode:

    def __init__(self):
        # Each node has: 
        # 1. children → mapping from char → next TrieNode
        # 2. isEnd → marks if a full word ends at this node
        self.children = {}
        self.isEnd = False 

class Trie:

    def __init__(self):
        # Root node represents an empty prefix
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        # Traverse each character of the word
        for ch in word:
            # If the character is not present in children, create a new TrieNode
            if ch not in node.children: #here we are checking key val. That is why we are able to compare char of word and children. But the value is TrieNode. it will have its own variables(children,isEnd)
                node.children[ch] = TrieNode()
            node = node.children[ch] # Move to the next node
        node.isEnd = True # mark end of word
        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        # Only true if this node is marked as a complete word
        return node.isEnd # true only if full word exists
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children: 
                return False
            node=node.children[ch]
         # All prefix characters matched
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
