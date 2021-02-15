class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegrees = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adj[pre].add(cur)
        
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        if not q:
            return []
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for successor in adj[course]:
                indegrees[successor] -= 1
                if indegrees[successor] == 0:
                    q.append(successor)
                    
        if len(res) == numCourses:
            return res
        else:
            return []
            
