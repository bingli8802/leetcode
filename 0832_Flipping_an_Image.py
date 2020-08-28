class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for a in A:
            a[:] = a[::-1]
            for i in range(len(a)):
                if a[i] == 0:
                    a[i] = 1
                elif a[i] == 1:
                    a[i] = 0
        return A
    
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for a in A:
            a[:] = a[::-1]
            for i in range(len(a)):
                a[i] = a[i] ^ 1
        return A
