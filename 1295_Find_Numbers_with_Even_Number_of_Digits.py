class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                ans += 1
        return ans
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        return sum(1 for num in nums if len(str(num)) % 2 == 0)
        # return sum(1 for num in nums if int(math.log10(num) + 1) % 2 == 0)
