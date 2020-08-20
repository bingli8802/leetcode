class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        parents = dict()
        for e in edges:
            # 判断如果节点不在dict里面，就把 (节点:父节点)这个map 添加到dict
            if e[1] not in parents:
                parents[e[1]] = e[0]
            # 如果节点已经在dict里：
            # 1. 如果这个节点的父节点不是0：就把 (父节点：节点)这个map 添加到dict
            # 2. 如果这个节点的父节点是0:就要把之前的map反转 变成(节点:父节点)这个map 再把(节点：0)这个map 添加到dict
            else:
                if e[0] != 0:
                    parents[e[0]] = e[1]
                else:
                    # 反转
                    parents[parents[e[1]]] = e[1]
                    parents[e[1]] = e[0]        
        paths = set()
        for i in range(len(hasApple)):
            if hasApple[i]:
                p = i
                # 根据p的值向上找根节点 直到p=0
                while (p != 0):
                    paths.add(p)
                    print paths
                    # p变为当点节点的父节点
                    p = parents[p]
        return len(paths)*2
    
class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        parents = dict()
        for e in edges:
            # 判断如果节点不在dict里面，就把 (节点:父节点)这个map 添加到dict
            if e[1] not in parents:
                parents[e[1]] = e[0]
            # 如果节点已经在dict里：
            # 1. 如果这个节点的父节点不是0：就把 (父节点：节点)这个map 添加到dict
            # 2. 如果这个节点的父节点是0:就要把之前的map反转 变成(节点:父节点)这个map 再把(节点：0)这个map 添加到dict
            else:
                if e[0] != 0:
                    parents[e[0]] = e[1]
                else:
                    # 反转
                    parents[parents[e[1]]] = e[1]
                    parents[e[1]] = e[0]        
        all_paths = set()
        for i in range(len(hasApple)):
            if hasApple[i]:
                p = i # p = 2,4,5
                # 根据p的值向上找根节点 直到p=0
                while p!=0:
                    all_paths.add((parents[p], p)) 
                    # all_paths = ((0,2),(1,4),(0,1),(1,5))
                    # p变为当点节点的父节点
                    p = parents[p] # p = 0,1,0,1
        return len(all_paths)*2

