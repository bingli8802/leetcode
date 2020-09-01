class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b, count_a, count_b = 0, 0, 0, 0 # 设定1号众数和2号众数
        res = []

        for i in nums:
            if a == i: # 频数统计的优先顺序要大于频数为0的判断
                count_a += 1
                continue
            if b == i:
                count_b += 1
                continue
            if count_a == 0:
                a = i
                count_a = 1
                continue
            if count_b == 0:
                b = i
                count_b = 1
                continue
            count_a -= 1
            count_b -= 1        

        count_a, count_b = 0, 0 # 重置计数器
        for j in nums: # 再检验
            # 这里一定要用else if
            # 因为可能出现[0,0,0]这种用例，导致两个cand是一样的，写两个if结果就变为[0,0]了
            if j == a:
                count_a += 1
            elif j == b:
                count_b += 1
        if count_a > len(nums)/3:
            res.append(a)
        if count_b > len(nums)/3:
            res.append(b)
        return res
