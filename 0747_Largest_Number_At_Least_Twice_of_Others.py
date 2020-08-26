class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = max(nums)
        for i in nums:
            if i != maxi and i * 2 > maxi:
                return -1
        return nums.index(maxi)
    
    # The all() function returns True if all items in an iterable are true, otherwise it returns False. 
    # If the iterable object is empty, the all() function also returns True.
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        m = max(nums)
        if all(m >= x*2 for x in nums if x != m):
            return nums.index(m)
        return -1


