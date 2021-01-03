class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        """
        s.reverse()
        """
        """
        s[:] = s[::-1]
        """
        mid = int(len(s)/2)
        j = len(s) - 1
        for i in xrange(mid):
            s[i], s[j-i] = s[j-i], s[i]
            
    # 类似二分查找  
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
