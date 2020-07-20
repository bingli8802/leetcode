class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """      
        if n == 0:
            return 0
        
        left = 0
        # left = 1
        right = n
        
        # while left < right:
        #     target =  (left + right + 1)/2
        #     if target*(target+1)/2 == n:
        #         return target
        #     elif target*(target+1)/2 > n:
        #         right = target - 1
        #     elif target*(target+1)/2 < n: 
        #         left = target
        # return left
    
        while left <= right:
            target =  (left + right + 1)/2
            if target*(target+1)/2 == n:
                return target
            elif target*(target+1)/2 > n:
                right = target - 1
            elif target*(target+1)/2 < n: 
                left = target + 1
        return right

