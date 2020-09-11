class Solution(object):
    # 自己算法很慢
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if len(arr) == arr[-1]:
            return arr[-1] + k
        cnt = 0
        for i in range(1, arr[-1]):
            if i not in arr:
                cnt += 1
            if cnt == k:
                return i
        return arr[-1] + (k-cnt)
    
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(arr)):
            distance = arr[i] - i
            if k < distance:
                return arr[i] - (distance-k)
        return arr[-1]-distance+k+1
