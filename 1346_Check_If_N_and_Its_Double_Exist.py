class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        li = []
        for i in arr:
            if i % 2 == 0 and i / 2 in li or i * 2 in li:
                return True
            li.append(i)
        return False
    
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            if arr[i]*2 in arr and i != arr.index(arr[i]*2):
                return True
        return False

