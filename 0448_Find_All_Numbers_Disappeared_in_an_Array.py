class Solution(object):
    # 自己解法 超时
    # list的查找(int)操作时间复杂度是O(n), 再加上外面的for循环就是O(n^2)了。哈希表查找操作是O(1)
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                res.append(i)
        return res
    
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not 
        # really concerned with the frequency of numbers.
        hash_table = {}
        
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table. 
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)         
        return result
    
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Response array that would contain the missing numbers
        res = []
        # Iterate over each of the elements in the original array
		# 第一遍扫描，根据数组的值找到对应的下标，比如3对应下标2
		# 将arr[2]设置成负数 
            # Treat the value as the new index
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
        for i in nums:
		    index = abs(i)-1
		    if nums[index]>0:
				nums[index] *= -1
		# 第二遍扫描，找到所有非负数，非负数所在的下标+1，即为缺失的数字
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array
        for i in xrange(len(nums)):
			if nums[i]>0:
				res.append(i+1)
        return res
    
