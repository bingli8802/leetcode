class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ord('A') = 65
        res = 0
        for i in s:
            res = ord(i) - 64 + res * 26
        return res
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, 
               "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, 
               "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
        
        return sum([26**i*dct[j] for i, j in enumerate(s[::-1])])
        # return sum([(26**i) * (ord(c)-64) for i, c in enumerate(s[::-1])])


        
