class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        #Step 1: Build pattern_map
        pattern_map = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)
        
        #Step 2: BFS
        queue = deque([(beginWord,1)])
        visited = set([beginWord])

        while(queue):
            word,level = queue.popleft()
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]

                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return level + 1

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,level+1))
                
                #Important Optimization : to avoid multiple checks and save time. For large inputs, we may get TLE
                pattern_map[pattern] = []
        return 0 
