class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # [left, right] is the range for leftbound
        # [0,1,2,3,4] is the index
        # [1,2,3,4,5] length n = 5, if k = 3, the leftbound should no more than index n-k=2
        # means that leftbound can only fall in range[1,2,3]
        
        left = 0
        right = len(arr) - k       
        
        while left < right:
            mid = left + (right - left) // 2
            # 尝试从长度为 k + 1 的连续子区间删除一个元素 从而定位左区间端点的边界值
            # if x is closer than arr[mid+k]
            # e.g. 极端例子 [1,2,3,4,5] x = 8 
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            # if x is closer than arr[mid], right should be mid
            # e.g. 极端例子 [1,2,3,4,5] x = -2
            elif x - arr[mid] <= arr[mid+k] - x:
                right = mid
        return arr[left: left + k]

