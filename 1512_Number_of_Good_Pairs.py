class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in set(nums):
            count_i = nums.count(i)
            ans += count_i * (count_i - 1) / 2
        return ans
    
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
    
    # 最快
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        m = collections.Counter(nums)
        # m = Counter({1: 3, 3: 2, 2: 1})
        return sum(v * (v - 1) // 2 for k, v in m.items())


