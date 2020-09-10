class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        SA = sum(A)
        SB = sum(B)
        sub = (SB - SA)/2
        for i in set(A):
            if i + sub in set(B):
                return [i, i+sub]
