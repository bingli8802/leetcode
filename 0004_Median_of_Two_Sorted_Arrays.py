class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def helper(nums1,nums2,k): #本质上是找第k小的数
            if (len(nums1) <len(nums2)):
                nums1, nums2 = nums2 , nums1 #保持nums1比较长
            if (len(nums2) == 0):
                return nums1[k-1] # 短数组空，直接返回
            if (k == 1):
                return min(nums1[0],nums2[0])  #找最小数，比较数组首位
            t = min(k//2,len(nums2)) # 保证不上溢
            if (nums1[t-1] >= nums2[t-1] ):
                return helper(nums1,nums2[t:],k-t)
            else:
                return helper(nums1[t:],nums2,k-t)
            
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2  
            
        if k1 == k2:
            return helper(nums1, nums2, k1)
        else:
            return (helper(nums1,nums2,k1) + helper(nums1,nums2,k2)) /float(2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """        
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)    
        k = (n1 + n2 + 1) / 2
        left = 0
        right = n1
        
        while left < right :     
            m1 = left + (right - left) / 2  # 左边需要的个数
            m2 = k - m1  # 右边需要的个数
            # print m1, m2       
            if nums1[m1] < nums2[m2-1]:  # 左边的数不够 需要右移 
                left = m1 + 1
            elif nums1[m1] >= nums2[m2-1]: # 左边的数多 需要左移
                right = m1
                
        m1 = left
        m2 = k - m1 
                
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 <n2 else float("inf"))
        return (c1 + c2) / float(2)


# [1,2,3,4, 5,6,7,8] mid = (4 + 4)/2 = 4
# [1,2,3,4,   5,6,7] mid = (3 + 4)/2 + 1 = 4
# so rounded up 向上取整 mid = (n1 + n2 + 1)/2
         
                
        
        
        
        
