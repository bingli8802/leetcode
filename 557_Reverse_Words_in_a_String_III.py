
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        li = s.split(" ")
        for i in li:
            """reverse each string in the list"""
            """i = i[::-1]"""
            i = "".join(reversed(i))
            ret.append(i)
        return " ".join(ret)
