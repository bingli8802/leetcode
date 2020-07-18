class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = s.strip().split(" ")
        
        print li
        
        if len(li) == 0:
            return 0
        else:
            return len(li[-1])
