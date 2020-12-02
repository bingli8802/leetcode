class Solution(object):
    # dp超时
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        M = [0] * n
        j = n - 1
        for i in range(n-2, -1, -1):
            if nums[i] != 0:
                M[i] = 1 + min(M[j:j+nums[i]])
            else:
                M[i] = 1 + M[j]
            j = i
        return M[0]
    
    # 参考答案
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        jumps, curEnd, curFarthest = 0, 0, 0
        for i in range(length-1):
            curFarthest = max(curFarthest, i + nums[i])
            if i == curEnd:
                jumps+=1
                curEnd = curFarthest
        return jumps
    
    # 参考答案优化
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res, lastJumpFurthest, canJumpFurthest = 0, 0, 0
        for i in range(n-1):
            canJumpFurthest = max(canJumpFurthest, i + nums[i])
            if i == lastJumpFurthest:
                res+=1
                lastJumpFurthest = canJumpFurthest
                if canJumpFurthest >= n-1:
                    return res
        return res
