class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        half = self.myPow(x,n/2)
        rest = self.myPow(x,n%2)
        return rest*half*half
