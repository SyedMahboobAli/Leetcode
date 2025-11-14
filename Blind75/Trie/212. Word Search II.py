class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # store full word at terminal node
class Solution:
    def buildTrie(self,words : List[str]) -> TrieNode:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch]= TrieNode()
                node = node.children[ch]
            node.word = w
        return root
                

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #base case
        if not board or not board[0] or not words:
            return []

        rows,cols = len(board), len(board[0])
        root = self.buildTrie(words)
        found = []

        def dfs(r,c,node):
            ch = board[r][c]

            if ch not in node.children:
                return

            next_node= node.children[ch]
            #next_node can be last node which has 0 children and has word.
            # Found a word
            if next_node.word:
                found.append(next_node.word)
                # Prevent duplicate finds
                next_node.word = None

                #now the next_node has 0 children and word = None. This node is of no use. can be pruned. Check the advantages at the end
            
            # Mark visited
            board[r][c] = '#'
            #check 4 directions
            for dr,dc in ((0,-1),(0,1),(1,0),(-1,0)):
                nr,nc = r+dr, c+dc
                if(0<=nr<rows and 0<=nc<cols and board[nr][nc]!='#'):
                    dfs(nr,nc,next_node)

            # Restore
            board[r][c] = ch

            # Optional pruning: if next_node has no children, remove it to speed up future searches
            if not next_node.children:
                # deleting key from parent to allow garbage-collection/pruning of search space
                node.children.pop(ch, None) #Removes the key ch if it exists.  If ch is NOT in the dictionary, it returns None quietly. If the key does NOT exist, it raises a KeyError. We use this coz pruning happens inside DFS recursion, where timing is tricky and Another recursive path may have already pruned

        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root)
        return found

'''
Pruning does NOT remove anything needed.
It only deletes Trie nodes that no longer:
    represent any remaining word
    have any children that lead to a remaining word

the last node is removed first. slowly if the above node also has nothing {} and none (default) , then this is also pruned. Once pruned, the first base case in dfs is used to return: if ch not in node.children: return

This is why this pruning is one of the secret ingredients that makes top LeetCode submissions fast.

Summary (super short)
After DFS on a path, if a Trie node has no children left, it means no words use that prefix anymore.
So we delete the branch from its parent.
This saves huge redundant work in future DFS calls.
It never breaks correctness.
'''
