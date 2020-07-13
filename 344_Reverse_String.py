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
        for i in xrange(mid):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        
#         i = 0
#         j = len(s) - 1
#         while i < j:
#             s[i], s[j] = s[j], s[i]
#             i, j = i + 1, j - 1
