class Solution(object):
    # 第一种解法超时
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n <= 1:
            return res
        def ifPrime(num):
            for j in range(2, num):
                if num % j == 0:
                    return 0
            return 1
        for i in range(2,n):
            res += ifPrime(i)
        return res
    
    # 第二种解法超时
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n <= 1:
            return res
        def ifPrime(num):
            j = 2
            while j * j <= num:
                if num % j == 0:
                    return 0
                j += 1
            return 1
        for i in range(2,n):
            res += ifPrime(i)         
        return res
    
    # 思路：埃氏筛
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 定义数组标记是否是质数
        is_prime = [1] * n   
        count = 0
        for i in range(2, n):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                count += 1
                # 从 i*i 开始标记
                for j in range(i*i, n, i):
                    is_prime[j] = 0
        return count

