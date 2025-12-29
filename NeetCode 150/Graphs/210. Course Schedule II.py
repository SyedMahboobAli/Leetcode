class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Topological Sort using BFS
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        res = []
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []
