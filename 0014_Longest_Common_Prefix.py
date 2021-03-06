class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ""
        min_length = 0
        
        if len(strs) != 0:
            min_length = min(len(ele) for ele in strs)  
        
        for x in range(min_length):   
            for y in range(len(strs)-1):  
                if strs[y][0:x+1] != strs[y+1][0:x+1]:
                    return pre  
            pre = strs[0][0:x+1] 
        return pre
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0:
            return ""
        # min_len = float("inf")
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return res
            res += strs[0][i]
        return res
        
