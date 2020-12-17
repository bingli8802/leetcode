class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        # 先排序
        # important step !
        nums.sort()
        
        # The container that keep the size of the largest divisible subset that ends with X_i
        # dp[i] corresponds to len(EDS(X_i))
        dp = [0] * (len(nums))
        
        # 每次都用当前nums[i]去除i之前所有的数字 如果有更大值就更新maxSubsetSize
        """ Build the dynamic programming matrix/vector """
        for i, num in enumerate(nums):
            maxSubsetSize = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    maxSubsetSize = max(maxSubsetSize, dp[k])
            maxSubsetSize += 1
            dp[i] = maxSubsetSize
        
        # 找到最大dp值 以及在nums中的index
        """ Find both the size of largest divisible set and its index """ 
        maxSize, maxSizeIndex = max([(v, i) for i, v in enumerate(dp)])
        ret = []

        # 重建整除子集
        """ Reconstruct the largest divisible subset """ 
        # currSize: the size of the current subset
        # currTail: the last element in the current subset
        currSize, currTail = maxSize, nums[maxSizeIndex]
        for i in range(maxSizeIndex, -1, -1):
            # 这一步判断很关键
            if currSize == dp[i] and currTail % nums[i] == 0:
                ret.append(nums[i])
                currSize -= 1
                currTail = nums[i]
        # 不转成正序也可以
        return reversed(ret)
        # return ret
