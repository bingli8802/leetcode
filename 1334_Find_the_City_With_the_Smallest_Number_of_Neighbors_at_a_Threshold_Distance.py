class Solution(object):
    # 自己解法 没通过
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # eventually we need to get something like:
        # res = {0:[1], 1:[2, 3, 4], 2:[1, 3], 3:[1, 2]}
        
        # dic = {0:[(1,3)], 1:[(3,4), (2,1), (0,3)], 2:[(1,1), (3,1)], 3:[(1,4), (2,1)]}
        dic = defaultdict(list)
        for x, y, z in edges:
            dic[x].append((y, z))
            dic[y].append((x, z))

        # print dic
        res = defaultdict(list)
        
        for k in dic.keys():
            q = deque([k])
            tmp = {k:0}
            while q:
                node = q.popleft()
                dist = tmp[node]
                # print node, dist
                for nei, nei_dist in dic[node]:
                    # print node,dic[node], nei, q, tmp
                    new_dist = dist + nei_dist
                    # if nei == k or new_dist > distanceThreshold:
                    #     continue
                    # else:
                    if nei in tmp and new_dist < tmp[nei]:
                        tmp[nei] = new_dist
                        continue
                    elif nei not in tmp and new_dist <= distanceThreshold:
                        res[k].append(nei)
                        q.append(nei)
                        tmp[nei] = new_dist
                        # print q
        print res
        nodes = [i for i in range(n)]
        diff = [i for i in range(n) if i not in res.keys()]
        print diff
        if diff:
            return max(diff)

        min_dist = float('inf')
        ret = []
        # [(0, [1, 2]), (1, [0, 2, 3]), (2, [1, 3, 0]), (3, [1, 2])]
        distance = res.items()
        print distance
        for tp in distance:
            if len(tp[1]) < min_dist:
                min_dist = len(tp[1])
                ret = [tp[0]]
            elif len(tp[1]) == min_dist:
                ret.append(tp[0])
        # print ret
        return max(ret)
    
    # 网友 Dijkstra    
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """  
        g = collections.defaultdict(list) 
        for i , j , w in edges:
            g[i].append((j,w))
            g[j].append((i,w))    
        def neighbours(i):    
            heap = [(0,i)]
            d = {}
            while heap:
                distance , node = heappop(heap)
                if node in d:
                    continue
                if node != i:
                    d[node] = distance
                for nei,w in g[node]:
                    if nei in d:
                        continue
                    if distance+w <= distanceThreshold:
                        heappush(heap,(distance+w,nei))           
            return len(d)                
        return max([(neighbours(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]
     
    # Floyd Warshall
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dp = [[float('inf')] * n for _ in range(n)]
        
        for x, y, z in edges:
            dp[x][y] = z
            dp[y][x] = z
        
        for num in range(n):
            dp[num][num] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                    
        res = 0
        min_len = float('inf')
        for idx, val in enumerate(dp):
            tmp = [dist for dist in val if dist <= distanceThreshold]
            if len(tmp) <= min_len:
                res = idx
                min_len = len(tmp)
        return res
            
        
        # res,count=0,n+1
        # for i in range(n):
        #     cur=0
        #     for j in range(n):
        #         if dis[i][j]<=distanceThreshold:
        #             cur+=1
        #     if cur<=count:
        #         res,count=i,cur
        # return res



