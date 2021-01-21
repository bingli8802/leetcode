class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        li = [elem for elem in s if str(elem).isalnum()]
        
        # if li[:] == li[::-1]:
        #     return True
        # else:
        #     return False
        
        return li[:] == li[::-1]
    
    # 双指针做法
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
        return True
