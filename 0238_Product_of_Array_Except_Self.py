class Solution(object):
    # 两个数组分别存储左边和右边乘积
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        L = [1] * n
        R = [1] * n
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        res = []
        for i in range(n):
            res.append(L[i]*R[i])
        return res
    
    # 一个数组存储左边成绩 右边使用一个变量 从后往前更新L
    # 效率100%
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        L = [1] * n
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        r = 1
        for i in range(n-1, -1, -1):
            L[i] *= r
            r *= nums[i]
        return L
