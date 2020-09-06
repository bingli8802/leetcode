class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, value in enumerate(nums):
            dict[value] = index
        for i, v in enumerate(nums):
            diff = dict.get(target - v)
            if diff is not None and i != diff:
                return [i, diff]
    # 改进     
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, v in enumerate(nums):
            diff = dict.get(target - v)
            if diff is not None:
                return [i, diff]
            dict[v] = i
        

