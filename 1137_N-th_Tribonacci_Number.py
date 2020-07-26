# class Solution:
#     def __init__(self):
#         self.dp = {}
        
#     def tribonacci(self, n):
#         if n == 0:
#             return 0
#         if n == 1 or n == 2:
#             return 1
#         try:
#             return self.dp[n]
#         except:
#             self.dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
#             return self.dp[n] 

ans = {0:0, 1:1, 2:1}
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n in ans:
            return ans[n]
        else:
            ans[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return ans[n]
