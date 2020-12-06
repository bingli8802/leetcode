class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.sums = [0]
        # 利用append 解决空间问题
        for k in range(n):
            self.sums.append(self.sums[k] + nums[k])
    # 超时
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         n = len(self.nums)
#         M = [0] * (n+1)
#         for k in range(1, n):
#             M[k] = M[k-1] + self.nums[k-1]
            
#         ret = M[j+1] - M[i]
#         return ret
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """ 
        return self.sums[j+1] - self.sums[i]
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
