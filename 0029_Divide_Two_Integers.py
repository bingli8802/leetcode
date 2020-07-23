class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """        
        m = long(abs(dividend))
        n = long(abs(divisor))
        res = 0
        
        if( (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0) ):
            sign = 0
        else:
            sign = 1
        
        m = long(abs(dividend))
        n = long(abs(divisor))
        res = 0
        
        while m >= n:
            t = n
            p = 1
            while m >= (t<<1):
                t = t<<1
                p = p<<1
            res = res + p
            m = m - t
        
        if sign == 1:
            return max(min(-res, (1 << 31) - 1), -1 << 31)
        else:
            return max(min(res, (1 << 31) - 1), -1 << 31)
