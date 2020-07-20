class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        new_nums1 = set(nums1)
        new_nums2 = set(nums2)
        
        if len(new_nums1) <= len(new_nums2):
            return [i for i in new_nums1 if i in new_nums2]
        else:
            return [i for i in new_nums1 if i in new_nums2]
