class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) > len(nums)/2:
                return i
            
    # Moore投票算法 相互抵消
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        candidate = nums[0]

        for num in nums[1:]:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
    
    # # 排序
    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     nums.sort()
    #     return nums[len(nums)/2]
