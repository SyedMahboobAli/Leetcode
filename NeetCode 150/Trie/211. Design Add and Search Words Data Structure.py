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
        def dfs(node,index):
            if index == len(word):
                return node.endofWord
            
            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child,index+1):#since I am searching for one true case. Then break the loop and return
                        return True
                return False #if no child is true, return False
                        
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch],index+1)
        return dfs(self.root,0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
