class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        i = 0
        while i < len(arr):
            if len(arr[i:]) < m * k:
                return False
            j = 1
            while j < k:
                if arr[i:i+m] != arr[i+m*j:i+m*(j+1)]:
                    i += 1
                    break
                elif arr[i:i+m] == arr[i+m*j:i+m*(j+1)]:
                    j += 1
            if j == k:
                return True
            
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """      
        n = len(arr)
        if n < m * k:
            return False
        for i in range(n - m + 1):
            if arr[i:i+m*k] == arr[i:i+m] * k:
                return True
        return False
        
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for i in range(len(arr)-m):
            if len(arr[i:]) < m * k:
                return False
            if arr[i:i+m*k] == arr[i:i+m] * k:
                return True
        return False

                    
