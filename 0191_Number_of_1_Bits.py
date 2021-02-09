class Solution(object):
    # 和1做 & 操作 再右移一位
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res
        
