class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)
    # 从后往前遍历
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        p = m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[p] = nums2[j]
                j -= 1
                p -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
                p -= 1
        nums1[:j+1] = nums2[:j+1]
        
