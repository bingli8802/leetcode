class Solution(object):
    # 自己解法快一点
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        dic = collections.Counter(nums)
        s = set(nums)
        for i in s:
            if k > 0 and i + k in s or k == 0 and dic[i] > 1:
                res += 1
        return res
                
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res

