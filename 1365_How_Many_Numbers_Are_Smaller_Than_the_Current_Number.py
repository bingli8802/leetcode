class Solution(object):
    # 暴力解法
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            cnt = 0
            for j in nums:
                if j < i:
                    cnt += 1
            res.append(cnt)
        return res
    # 排序
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = sorted(nums)
        print new
        L = []
        for num in nums:
            L.append(new.index(num))
        return L

