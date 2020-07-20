class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        
        while i<=j: 
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                x = s[i:j]
                y = s[i+1:j+1]
                
                if x[:] == x[::-1] or y[:] == y[::-1]: 
                    return True
                else:   
                    return False
                
        return True
