class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = defaultdict(list)
        for i in range(len(nums)):
            dict[nums[i]].append(i)
        degree = 0
        subarray = dict.values()[0]
        for value in dict.values():
            if len(value) > degree:
                degree = len(value)
                subarray = value
            elif len(value) == degree:
                if value[-1] - value[0] < subarray[-1] - subarray[0]:
                    subarray = value
        res = subarray[-1] - subarray[0] + 1
        return res
    
    # 官方题解
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans

