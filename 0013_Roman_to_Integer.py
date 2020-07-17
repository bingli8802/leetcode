class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = list(s)
        ret = 0
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for i in xrange(len(li)):
            if i < len(li) - 1 and dict[li[i]] < dict[li[i+1]]:
                ret -= dict[li[i]]
            else:
                ret += dict[li[i]]
        return ret
