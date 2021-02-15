class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0 for _ in range(numCourses)]
        adjancy = [[] for _ in range(numCourses)]
        
        for cur, pre in prerequisites:
            indegree[cur] += 1
            adjancy[pre].append(cur)
        
        q = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        if not q:
            return False
        cnt = 0
        while q:
            course = q.popleft()
            cnt += 1
            for adj in adjancy[course]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
        return cnt == numCourses
