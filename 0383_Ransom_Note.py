class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        
        if not ransomNote:
            return True
        
        dic = defaultdict(int)
        
        for i in ransomNote:
            dic[i] += 1
            
        for k in dic.keys():
            if magazine.count(k) < dic[k]:
                return False
        return True
    
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a = dict(collections.Counter(ransomNote))
        for k, v in a.items():
            if magazine.count(k) < v:
                return False
        return True

