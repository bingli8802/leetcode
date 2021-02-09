class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def days(m):
            cnt = 1
            total = 0 
            for w in weights:
                if total + w > m:
                    cnt += 1
                    total = w
                elif total + w <= m:
                    total += w
            return cnt
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left) / 2
            if days(mid) > D:
                left = mid + 1
            elif days(mid) <= D:
                right = mid
        return left
