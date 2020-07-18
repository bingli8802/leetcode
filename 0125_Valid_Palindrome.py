class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        li = [elem for elem in s if str(elem).isalnum()]
        
        if li[:] == li[::-1]:
            return True
        else:
            return False
