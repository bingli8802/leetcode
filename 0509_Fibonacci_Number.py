class Solution(object):
    # 递归太费时 
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
    # 自下而上迭代
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        cur = 0
        prev1 = 0
        prev2 = 1
        for i in range(2, N+1):
            cur = prev1 + prev2
            prev1 = prev2
            prev2 = cur
        return cur
    
    # 自下而上记忆法 速度最快
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N):
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]
    
    # 自下而上记忆法 速度最快
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        def memoize(N):
            cache = {0: 0, 1: 1}
            # Since range is exclusive and we want to include N, we need to put N+1.
            for i in range(2, N+1):
                cache[i] = cache[i-1] + cache[i-2]
            return cache[N]
        if N <= 1:
            return N
        return memoize(N)
