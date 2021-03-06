class Solution(object):
    # dp超时 O(n^2)
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [0] * n
        dp[-1] = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if dp[j] == 1 and nums[i] >= j-i:
                    dp[i] = 1
                    break
        return dp[0]
    
    # lc答案 一次循环 解决超时问题
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        index = n - 1
        for i in range(n-2,-1,-1):
            if index-i <= nums[i]:
                index = i
                dp[index]=True
        return dp[0]
    
    # 贪心算法 一次循环
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        rightmost = 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
    
    # 贪心算法 一次循环 更好理解
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        rightmost = 0
        for i in range(n-1):
            rightmost = max(rightmost, i + nums[i])
            if rightmost <= i:
                return False
        return rightmost >= n - 1

