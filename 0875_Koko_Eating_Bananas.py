class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2

            if self.__calculate_sum(piles, mid) > H:
                left = mid + 1
            else:
                right = mid
        return left

    def __calculate_sum(self, piles, speed):
        res = 0
        for pile in piles:
            res += (pile + speed - 1) // speed
        return res
    
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        # calculate total time to finish all the bananas
        def calculate_time(piles, speed):
            h = 0
            for pile in piles:
                h = h + (pile + speed - 1)/speed # 注意 向上取整  
            return h
        
        # koko can eat minimum 1 banana and up to max(piles) per hour
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + (right - left)/2
            tm = calculate_time(piles, mid)
            if tm > H:
                left = mid + 1
            elif tm <= H:
                right = mid
        return left
    


