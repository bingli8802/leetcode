class Solution(object):
    # 自己解法 很慢 O(n^2)
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr)-1:
            if arr[i] == 0: 
                arr[i+1:] = [0] + arr[i+1:-1]
                i += 2
            else:
                i += 1
    # 改进 pop insert O(n)
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.pop(-1)
                arr.insert(i, 0)
                i += 2
            else:
                i += 1
                
