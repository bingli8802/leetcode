class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = list(s)
        lt = list(t)
        
        ds = dict(collections.Counter(ls))
        dt = dict(collections.Counter(lt))
        
        if sorted(ds.keys()) != sorted(dt.keys()):
            return False
        for k in ds.keys():
            if ds[k] != dt[k]:
                return False
        return True
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)
    
