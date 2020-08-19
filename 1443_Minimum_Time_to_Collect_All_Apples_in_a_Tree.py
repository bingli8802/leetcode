class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        parents = dict()
        # 先创建一个map 每个节点指向父节点
        for edge in edges: 
            parents[edge[1]] = edge[0] # parents = {1:0, 2:0, 4:1, 5:1, 3:2, 6:2}
        all_paths = set()
        for i in range(len(hasApple)):
            if hasApple[i]:
                p = i # p = 2,4,5
                # 根据p的值向上找根节点 直到p=0
                while p!=0:
                    all_paths.add((parents[p], p)) # all_paths = ((0,2),(1,4),(0,1),(1,5))
                    # p变为当点节点的父节点
                    p = parents[p] # p = 0,1,0,1
        return len(all_paths)*2

