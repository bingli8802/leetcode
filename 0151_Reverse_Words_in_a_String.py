class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = s.split() 
        i = 0
        j = len(li) - 1
        while i < j:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
        return " ".join(li)
        
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])
