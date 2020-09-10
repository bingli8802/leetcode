class Solution(object):
    # 自己解法很慢
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = defaultdict(list)
        for i, v in enumerate(nums):
            dic[v].append(i)
        print dic
        for val in dic.values():
            if len(val) >=2:
                for m in range(len(val)-1):
                    for n in range(m+1,len(val)):
                        if abs(val[m]-val[n]) <= k:
                            return True
        return False
    
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict and i - dict[nums[i]] <= k:
                return True
            # 如果nums[i]不在dict里 或者 当前距离大于k 就更新i的值
            elif nums[i] not in dict or i - dict[nums[i]] > k:
                dict[nums[i]] = i
            # dict[nums[i]] = i
        return False

