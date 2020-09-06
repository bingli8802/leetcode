class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        li = [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]
        half = len(A) / 2
        for i in range(1, half, 2):
            if half % 2 == 0:
                li[i], li[i + half - 1] = li[i + half - 1], li[i]
            elif half % 2 == 1:
                li[i], li[i + half] = li[i + half], li[i]
        return li
    
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

