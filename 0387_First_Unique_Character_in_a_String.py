class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        res = float('inf')
        dic = defaultdict(list)
        for i, v in enumerate(s):
            dic[v].append(i)
        for val in dic.values():
            if len(val) == 1:
                res = min(res, val[0])
        if res == float('inf'):
            return -1
        else:
            return res
        
    # if index are the same     
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """    
        for i in s:
            if s.find(i) == s.rfind(i):
                return s.find(i)
        return -1
