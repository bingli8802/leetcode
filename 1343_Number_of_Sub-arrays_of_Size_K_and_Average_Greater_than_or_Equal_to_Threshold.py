class Solution(object):
    # 自己解法 超时
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0
        n = len(arr)
        target = k * threshold
        for i in range(n-k+1):
            if sum(arr[i:i+k]) >= target:
                res += 1
        return res
    
    # 滑动窗口 最优解
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        total = sum(arr[:k])
        target = k * threshold
        n = len(arr)
        res = 1 if total >= target else 0
        for i in range(k, n):
            total += arr[i] - arr[i-k]
            if total >= target:
                res += 1
        return res
