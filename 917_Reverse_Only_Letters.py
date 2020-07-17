class Solution(object):
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
