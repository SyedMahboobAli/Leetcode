class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # store full word at terminal node
class Solution:
    def buildTrie(self,words: List[str]) -> TrieNode:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
            node.word = w
        return root
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        rows,cols = len(board), len(board[0])
        root = self.buildTrie(words)
        found = []
        
        def dfs(r,c,node):

            ch = board[r][c]
            
            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            #next_node can be last node which has 0 children and has word.
            # Found a word
            if next_node.word:
                found.append(next_node.word)
                next_node.word = None # Prevent duplicate finds
            
            #now the next_node has 0 children and word = None. This node is of no use. can be pruned. Check the advantages at the end
            # Mark visited
            board[r][c] = '#'
            #check 4 directions
            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr,nc = r+dr, c+dc

                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != '#':
                    dfs(nr,nc,next_node)
            # Restore
            board[r][c] = ch

            # Optional pruning: if next_node has no children, remove it to speed up future searches
            if not next_node.children:
                node.children.pop(ch,None) #we are also adding None for default if node already pruned by other recursive calls
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    dfs(i,j,root)
        return found



