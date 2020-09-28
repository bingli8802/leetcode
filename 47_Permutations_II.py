class Solution(object):
    # 回溯算法 和46题思路一样
    # 不同地方是消除重复 写下两个例子就能明白了
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 先排序
        nums.sort()
        n = len(nums)
        res = []
        def helper(li, tmp_li, cnt):
            if cnt == n:
                res.append(tmp_li)
            for i in range(len(li)):
                # 判断重复数字
                if i > 0 and li[i] == li[i-1]:
                    continue
                helper(li[:i] + li[i+1:], tmp_li + [li[i]], cnt + 1)
        helper(nums, [], 0)
        return res
    
    # 效率很低
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        def helper(nums, temp_list, length):
            # 判断重复数字
			if length == n and temp_list not in res:
				res.append(temp_list)
			for i in range(len(nums)):
				helper(nums[:i] + nums[i + 1:], temp_list + [nums[i]], length + 1)
        helper(nums, [], 0)
        return res


