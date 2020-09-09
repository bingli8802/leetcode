class Solution(object):
    # counter效率低
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = collections.Counter(arr)
        for i in c:
            # if c[i] > len(arr)/4:
            if c[i] * 4 > len(arr):
                return i
    # 二分查找提高效率
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        span = n // 4 + 1
        for i in range(0, n, span):
            # 把arr[i]插入到arr[i]左边返回的index
            iter_l = bisect.bisect_left(arr, arr[i])
            # 把arr[i]插入到arr[i]右边返回的index
            iter_r = bisect.bisect_right(arr, arr[i])
            # 3，7
            if iter_r - iter_l >= span:
                return arr[i]

