class Solution(object):
    # O(n^2)
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == 3:
                        return True
        return False
    
    # O(n)
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = second_smallest = float('inf')
        for num in nums:
            if num < smallest:
                smallest = num
            if smallest < num < second_smallest:
                second_smallest = num
            if num > second_smallest:
                return True
        return False
