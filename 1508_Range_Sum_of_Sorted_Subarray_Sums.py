class Solution(object):
    # O(n^2logn)
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        li = []
        for i in range(n):
            li.append(nums[i])
            for j in range(i+1, n):
                li.append(li[-1] + nums[j])
        li.sort()
        res = sum(li[left-1:right])
        return res % (10**9 + 7)
    
    # 前缀和解法
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        prefix_and = [0]
        pre_and = 0
        for num in nums:
            pre_and += num
            prefix_and.append(pre_and)
        length = len(prefix_and)
        subarray_and = []
        for i in range(length):
            for j in range(i + 1, length):
                subarray_and.append(prefix_and[j] - prefix_and[i])
        subarray_and.sort()
        return sum(subarray_and[left - 1:right]) % (10**9 + 7)

