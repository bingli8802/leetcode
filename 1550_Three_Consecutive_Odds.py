class Solution(object):
    # 稍微慢一点
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        for i in range(n - 2):
            if all(j % 2 == 1 for j in arr[i:i+3]):
                return True
        return False
    
    # 算法快 接近100%
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        for i in range(n - 2):
            if arr[i] & 1 and arr[i + 1] & 1 and arr[i + 2] & 1:
                return True
        return False

