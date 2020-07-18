class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        h,n = len(haystack),len(needle)
        
        if n == "":
            return 0
        
        else:
            for i in range(h-n+1):
                if needle == haystack[i:i+n]:
                    return i
            return -1


