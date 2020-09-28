class Solution(object):
    # 回溯 思路
    # 每次都拿出一个数字放进tmp里 当长度等于n的时候 把结果append到res
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        def helper(li, tmp_li, cnt):
            if cnt == n:
                res.append(tmp_li)
            for i in range(len(li)):
                helper(li[:i] + li[i+1:], tmp_li + [li[i]], cnt + 1)
        helper(nums, [], 0)
        return res
