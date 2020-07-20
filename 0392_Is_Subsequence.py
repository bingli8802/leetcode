class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        
        while i < len(s) and i < len(t):
            if s[i] in t[i:]:
                i += 1
            else:
                return False
        return True
            
