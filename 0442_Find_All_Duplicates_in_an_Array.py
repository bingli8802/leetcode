class Solution(object):
    # 自己解法很慢
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        if len(nums) <= 1:
            return []
        if nums[-1] != nums[-2]:
            nums.pop(-1)
        return set(nums)
    
    # 原理：如果是相同的元素，那么以他们为索引的元素值一定是同一个值，因此可以修改该值来标记是否被访问过
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        rst = []
        for n in nums:
            # 因为我们是直接原地修改元素为负值来标记是否访问过，因此这里的n一定要取绝对值
            index = abs(n) - 1
            val = nums[index]
            if val < 0:
                # 如果元素值为负数，说明之前存在同一个索引为n的元素
                rst.append(abs(n))
            # 原地修改访问标志
            nums[index] = -nums[index]
        return rst
    
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] *= -1
            else:
                res.append(abs(n))
            print nums
        return res


