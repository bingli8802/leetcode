class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
#       对于本题，使用right = len(A)-1 或者right = len(A)都通过
#       因为要跟紧邻的右边的数字比较，这样初始化 right 的意义在于 mid+1 就不会越界了
        left = 0
        right = len(A)-1
        while left < right:
            mid = (left+right)/2
            if A[mid]>A[mid+1]:
                right = mid
            else:
                left = mid + 1
        return right
