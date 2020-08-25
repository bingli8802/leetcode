class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            if index[i] >= len(res):
                res.append(nums[i])
            else:
                res.insert(index[i], nums[i])
        return res
    
        def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res
