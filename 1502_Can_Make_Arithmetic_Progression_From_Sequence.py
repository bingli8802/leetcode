class Solution(object):
    # 等差数列
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) == 2:
            return True
        arr.sort()
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i-1] != arr[i+1] - arr[i]:
                return False
        return True
