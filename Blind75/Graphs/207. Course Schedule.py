class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list representation of the course graph
        adj={i:[] for i in range(numCourses)}
        # To take 'crs', you must first take 'pre'
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        
        # visited states:  Note: we can also use a set for this. We can add the number while visiting. if number in set => return False. At last remove from set.
        # 0 = unvisited, 1 = visiting (in current recursion stack), 2 = visited (fully processed)
        visited = [0 for _ in range(numCourses)] # or [0] * numCourses

        def dfs(course):
            # If course is being visited again in current DFS path → cycle detected
            if(visited[course] == 1):
                return False
            # If already processed completely, skip
            if(visited[course] == 2):
                return True
            
            # Mark current node as visiting
            visited[course]=1

            # Recursively visit all pre courses
            for nei in adj[course]:
                if not dfs(nei):
                     # Cycle found deeper in recursion
                    return False
                    
            # After exploring all neighbors, mark as fully processed
            visited[course]=2
            return True

        # Run DFS for all courses (graph may be disconnected)
        for i in range(numCourses):
            if not dfs(i):
                return False 
                  
        return True
