class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.endofWord = True

        

    def search(self, word: str) -> bool:
        def dfs(index,node):
            # base case: reached end of word
            if (index == len(word)):
                return node.endofWord
            
            ch = word[index]
            if ch == '.':
                # explore all possible children
                for child in node.children.values():
                    if dfs(index+1,child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(index+1,node.children[ch])

        return dfs(0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
