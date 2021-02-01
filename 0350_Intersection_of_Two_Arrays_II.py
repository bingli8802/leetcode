class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1) < len(nums2):
            dic1 = dict(collections.Counter(nums2))
            for i,v in enumerate(nums1):
                if v in dic1.keys():
                    if dic1[v] > 0:
                        res.append(v)
                        dic1[v] -= 1
                    else:
                        continue
                    
        else: 
            dic2 = dict(collections.Counter(nums1))
            for i,v in enumerate(nums2):
                if v in dic2.keys():
                    if dic2[v] > 0:
                        dic2[v] -= 1
                        res.append(v)
                    else:
                        continue
        return res
    
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        res = []
        dic1 = dict(collections.Counter(nums2))
        for i,v in enumerate(nums1):
            if v in dic1.keys():
                if dic1[v] > 0:
                    res.append(v)
                    dic1[v] -= 1
                else:
                    continue
        return res
    
    # 类似双指针
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
