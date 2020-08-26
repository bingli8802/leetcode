class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 1
        while b < len(nums):
            if nums[b] == nums[a]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
        return a+1
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 1
        while b < len(nums):
            if nums[a] == nums[b]:
                nums.pop(a)
            else:
                a += 1
                b += 1
        return len(nums)
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[j] == nums[i]:
                    nums.pop(j)
                else:            
                    break
            i = j
        return len(nums)
    
    


