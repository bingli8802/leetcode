class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = 1
        new_A = A
        
        while len(new_A) <= 10000 and len(B) <= 10000:
            if B in new_A:
                return i
            else:
                i = i+1
                new_A += A
        return -1
