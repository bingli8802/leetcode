class Solution(object):
    # 时间复杂度 O(n^2)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxLengthBeforeI(num):
            lstBeforeI = [dp[j] for j in range(num) if nums[j] < nums[i]]
            return max(lstBeforeI) if lstBeforeI else 0
        
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = 1 + maxLengthBeforeI(i)
        return max(dp)
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 二分法不会 先把答案copy过来
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: 
                    i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: 
                res += 1
        return res
    
    # 二分法不会 先把答案copy过来
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)

