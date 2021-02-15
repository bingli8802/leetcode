class Solution(object):
    # backtracking
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(f):             #深搜函数
            while d[f]:
                dfs(d[f].pop(0))#路径检索
            ans.insert(0, f)    #放在最前
            
        d = collections.defaultdict(list)   #邻接表
        for f, t in tickets:
            d[f] += [t]         #路径存进邻接表
        for f in d:
            d[f].sort()         #邻接表排序
        ans = []

        dfs('JFK')
        return ans
                
    # 欧拉路径 递归            
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """           
        def dfs(airport):
            while target[airport]:
                dfs(target[airport].pop())  # 从删除的节点继续搜索
            route.append(airport)  # 递归返回的时候，一次将路径加入到route中
            
        target = defaultdict(list)
        for start, end in sorted(tickets)[::-1]:  # 按字典逆序排序后，加入栈中
            target[start].append(end)
        # print target
        route = []
        dfs('JFK')
        return route[::-1]  # 逆序即最终路径

    # 欧拉路径 迭代写法，要会
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        target = defaultdict(list)
        for start, end in sorted(tickets)[::-1]:  # 按字典逆序排序后，加入栈中
            target[start].append(end)
        print target
        route = []
        stack = ['JFK']
        while stack:
            while target[stack[-1]]:
                stack.append(target[stack[-1]].pop())
                print stack
            route.append(stack.pop())
            print route
        return route[::-1]  # 逆序即最终路径

    
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # we need to get a mapping 
        dic = defaultdict(list)
        for start, end in (tickets):
            dic[start].append(end)
        for d in dic:
            dic[d].sort()
        print dic
        stack = ['JFK']
        res = []
        while stack:
            while dic[stack[-1]]:
                stack.append(dic[stack[-1]].pop(0))
            res.append(stack.pop())
        return res[::-1]
