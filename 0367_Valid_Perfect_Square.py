class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num <= 1:
            return True
        
        left = 1
        right = num
        
        while left < right:
            mid = (left+right+1)/2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                    right = mid - 1
            elif mid * mid < num:
                    left = mid
        return False
