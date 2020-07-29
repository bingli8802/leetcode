class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 原始数组长度
        length = len(nums)
        # 构建新的数组
        nums = nums + nums
        # 返回数组初始化为【-1，-1，-1】
        res = [-1] * length
        # 用来存储index的栈
        stack = []
        for i in range(0,len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                # 计算原来数组的index 并赋值比它大的元素
                res[index % length] = nums[i]
            # 每次都把当前元素的index放进栈
            stack.append(i % length)
        return res
