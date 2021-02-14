class Solution(object):
    # selection sort
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n-1):
            smallest = nums[i]
            idx = i
            for j in range(i+1, n):
                if nums[j] < smallest:
                    smallest = nums[j]
                    idx = j
            if smallest < nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
        return nums
    # insertion sort
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(1, n):
            for j in range(i,0,-1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        return nums
    # bubble sort
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    # merge sort
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        if n == 1:
            return nums
        mid = n/2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
                         
        l = 0
        r = 0
        
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        res += left[l:]
        res += right[r:]
        
        return res
    
    # quick sort
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lesser = []
        greater = []
        if len(nums) < 2:
            return nums
        for i in nums[1:]:
            if i < nums[0]:
                lesser.append(i)
            else:
                greater.append(i)
        
        return self.sortArray(lesser) + nums[:1] + self.sortArray(greater)    
        
        
