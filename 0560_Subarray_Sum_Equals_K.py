from collections import defaultdict

class Solution(object):
    # 东哥前缀和模版超时
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
            
        for i in range(1, n+1):
            for j in range(i):
                if preSum[i] - preSum[j] == k:
                    res += 1
        return res
    
    # 利用字典进行优化
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dic = {}
        # base case 一定要写
        dic[0] = 1
        sum0_i = res = 0
        for i in range(n):
            sum0_i += nums[i]
            if sum0_i - k in dic:
                res += dic[sum0_i - k]
            # 这里用dict.get(value, default value)避免keyerror
            dic[sum0_i] = dic.get(sum0_i, 0) + 1
        print dic 
        # {0: 1, 3: 1, 8: 2, 10: 1, 12: 1, 13: 1}
        return res
    
    # 利用字典进行优化 defaultdict
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        sum0_i = 0 
        res = 0
        # defaultdict字典为不存在的key赋值0
        dic = collections.defaultdict(int)
        # 什么都不取，前缀和一定为0，即前缀和为0 天然存在1种情况
        dic[0] = 1
        for i in range(n):
            # sum0_i 是0～i区间的和
            sum0_i += nums[i]
            # 不需要先判断是否存在key 
            # 如果不存在已经默认设置为0了，所以直接加就好了
            res += dic[sum0_i - k]
            # 需要注意的是，当前的前缀和要在最后更新，如果不这样子，k为0的时候会重复加
            dic[sum0_i] += 1
        print dic
        # {0: 1, 3: 1, 4: 0, 6: 0, 8: 2, 9: 0, 10: 1, 12: 1, 13: 1, -1: 0}
        return res

            
