class Solution(object):
    # 枚举法 O(n^3)
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        if len(rating) < 3:
            return 0
        res = 0
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)-1):
                for k in range(j+1,len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k] or rating[i] > rating[j] and rating[j] > rating[k]:
                        res += 1
        return res
    
    # 状态压缩 利用乘法原理 O(n^2)
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        res = 0
        for j in range(n):
            l = 0
            r = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    l += 1
            for k in range(j+1, n):
                if rating[j] < rating[k]:
                    r += 1
            res += l*r + (j-l)*(n-j-1-r)
        return res
