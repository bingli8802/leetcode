class Solution(object):
    # 用常规做法超时
    # 在一般情况下，当我们使用回溯法显示算法超时的时候，我们可以往动态规划的角度思考
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        res = []
        def helper(i, tmp):
            if sum(tmp) == target:
                res.append(tmp)
                return
            if sum(tmp) > target:
                return
            for j in range(n):
                if sum(tmp) > target:
                    break
                helper(j, tmp+[nums[j]])
        helper(0, [])
        return len(res)
    
    # 优化后的一维动态规划
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target < 0:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]
