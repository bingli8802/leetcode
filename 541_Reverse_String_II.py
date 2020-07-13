class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        li = list(s)
        
        for i in xrange(0,len(s), 2*k):
            """extended slice"""
            
            li[i:i+k] = li[i:i+k][::-1]
            """
            li[i:i+k] = reversed(li[i:i+k])
            """
        return "".join(li)        
