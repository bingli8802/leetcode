class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            mid = (left + right + 1) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid
        return left
