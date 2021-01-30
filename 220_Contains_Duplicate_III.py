class Solution(object):
    # 超时
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if j - i > k:
                    break
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False
