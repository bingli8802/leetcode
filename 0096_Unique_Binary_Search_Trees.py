# 如果1作为树根，左边有f(0)种情况，右边f(2)种情况，左右搭配一共有f(0)*f(2)种情况
# 如果2作为树根，左边有f(1)种情况，右边f(1)种情况，左右搭配一共有f(1)*f(1)种情况
# 如果3作为树根，左边有f(2)种情况，右边f(0)种情况，左右搭配一共有f(2)*f(0)种情况
# f(3) = f(0)*f(2) + f(1)*f(1) + f(2)*f(0)
# f(4) = f(0)*f(3) + f(1)*f(2) + f(2)*f(1) + f(3)*f(0)
# f(5) = f(0)*f(4) + f(1)*f(3) + f(2)*f(2) + f(3)*f(1) + f(4)*f(0)
# 对于每一个n，其式子都是有规律的 每一项两个f()括号里面的数字加起来都等于n-1
# f(0) = 1, f(1) = 1
# 卡特兰数
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        # 动态数组
        G = [0]*(n+1)
        G[0], G[1] = 1, 1
        # 根节点的范围从2到n+1
        for i in range(2, n+1):
            for j in range(i):
                G[i] += G[j] * G[i-j-1]
            # for j in range(1, i+1):
            #     G[i] += G[j-1] * G[i-j]
        return G[n]
    
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        store = [1,1] #f(0),f(1)
        if n <= 1:
            return store[n]
        for m in range(2,n + 1):
            s = m - 1
            count = 0
            for i in range(m):
                count += store[i] * store[s - i]
            store.append(count)
        return store[n]

    
    
