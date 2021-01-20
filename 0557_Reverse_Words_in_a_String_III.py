class Solution(object):
    # 原地修改
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(" ")
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        return " ".join(s_list)
    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        li = s.split(" ")
        for i in li:
            """reverse each string in the list"""
            i = i[::-1]
            # i = "".join(reversed(i)) # reversed特殊用法
            ret.append(i)
        return " ".join(ret)
