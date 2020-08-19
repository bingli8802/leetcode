# 迭代1 最容易理解的一个解法
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        l = len(edges)
        nums = [i for i in range(l + 1)]
        for item in edges:
            p1 = nums[item[0]]
            while p1 != nums[p1]:
                p1 = nums[p1]
            p2 = nums[item[1]]
            while p2 != nums[p2]:
                p2 = nums[p2]
            if p1 != p2:
                nums[p1] = item[1]
                print nums
            else:
                return item
# 迭代2
# class Solution(object):
#     def findRedundantConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """       
#         p = [[i] for i in range(len(edges) + 1)]  #并查集初始化 
#         for x, y in edges:
#             print "%s-%s" % (x,y)
#             print p
#             print "%s-%s" % (p[x],p[y])
#             if p[x] is not p[y]:            #如果两个集合地址不一样
#                 if len(p[x]) < len(p[y]):   #权重优化判断
#                     x, y = y, x
#                 p[x].extend(p[y])           #合并集合
#                 print p
#                 for z in p[y]:
#                     p[z] = p[x]             #修改元素集合标记的指针地址
#                 print p
#             else:
#                 return [x, y]
# 递归1
# class Solution(object):
#     def findRedundantConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """    
#         def findfa(x):
#             while x != father[x]:
#                 x = father[x]
#             return x        
#         father = {}
#         for u, v in edges:
#             if u not in father:
#                 father[u] = u
#             if v not in father:
#                 father[v] = v
#             pu, pv = findfa(u), findfa(v)
#             if pu == pv:
#                 return [u, v]
#             father[pu] = pv
# 递归2
# class Solution(object):
#     def findRedundantConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         # 用并查集，进来一对边，就查找两个节点的根节点，如果是一样的，那就不能要这对边，否则就增加这对边
#         pre = [0] * 1001 # 初始化所有的节点为单独的根节点
#         for edge in edges:
#             x = self.find(edge[0], pre)
#             y = self.find(edge[1], pre)
#             if x != y:
#                 pre[y] = x
#             else:
#                 return edge

#     def find(self, node, pre):
#         while pre[node] != 0:
#             node = pre[node]
#         return node



