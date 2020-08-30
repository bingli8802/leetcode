class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # 倒序比较 最后替换两端元素
        rmax = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            temp = arr[i]
            arr[i] = rmax
            rmax = max(temp, rmax)
        arr[0] = rmax
        arr[-1] = -1
        return arr
    
    # 很慢很慢     
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr

