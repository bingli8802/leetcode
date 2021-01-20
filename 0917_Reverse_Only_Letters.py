class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        j = len(S) - 1
        s = list(S)
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                if not s[i].isalpha():
                    i += 1
                elif not s[j].isalpha():
                    j -= 1
        return "".join(s)
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        new_S = []
        
        for i in S:
            if i.isalpha():
                new_S.insert(0,i)
        for c in range(len(S)):
            if not S[c].isalpha():
                new_S.insert(c,S[c])
        return "".join(new_S)
            
