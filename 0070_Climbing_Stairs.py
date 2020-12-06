class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 直接dp 空间复杂度O(n) 效率
        M = [1] * (n+1)
        M[1] = 1
        
        for i in range(2, n+1):
            M[i] = M[i-1] + M[i-2]
        return M[-1]
    
    # 空间复杂度O(1)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        
        first = 1
        second = 2
        
        for i in range(3, n+1):
            tmp = first + second
            first = second
            second = tmp
            
        return second
