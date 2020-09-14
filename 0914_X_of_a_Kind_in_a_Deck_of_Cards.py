class Solution(object):
    # 最大公约数内置函数
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # reduce
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
    
    # 最大公约数
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            if b == 0: 
                return a
            return gcd(b, a % b)
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) > 1
    
    # 枚举
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        n = len(deck)
        vals = collections.Counter(deck).values()
        for X in range(2, n+1):
            if n % X == 0:
                if all(v % X == 0 for v in vals):
                    return True
        return False
