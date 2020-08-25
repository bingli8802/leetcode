class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= maxi:
                res.append(True)
            else:
                res.append(False)
        return res
    
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool
        """
        maxi = max(candies)
        judge = []
        for i in candies:
            judge.append(i + extraCandies >= maxi)
        return judge

