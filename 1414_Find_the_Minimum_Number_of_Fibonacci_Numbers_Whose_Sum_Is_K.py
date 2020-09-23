class Solution(object):
    # 自己解法
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 1
        li = [1,1]
        SUM = li[-1] + li[-2]
        while SUM < k:
            SUM = li[-1] + li[-2]
            if SUM <= k:
                li.append(SUM)
        cnt = 0
        rem = k
        i = len(li) - 1
        
        while rem != 0:
            rem -= li[i]
            if rem == 0:
                cnt += 1
                return cnt
            elif rem > 0:
                cnt += 1
                i -= 1
            else:
                rem += li[i]
                i -= 1
        return cnt
    
    # 自己解法 改进
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 1
        li = [1,1]
        SUM = li[-1] + li[-2]
        while SUM <= k:
            li.append(SUM)
            SUM = li[-1] + li[-2]
        cnt = 0
        rem = k
        i = len(li) - 1
        
        while rem != 0:
            if li[i] <= rem:
                rem -= li[i]
                cnt += 1
            if rem == 0:
                return cnt
            i -= 1
        return cnt
    
    # 官方解法
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        a = b = 1
        fibo = [a, b]
        while a + b <= k:
            fibo.append(a + b)
            a, b = b, a + b
        ans = 0
        for num in fibo[::-1]:
            if k >= num:
                ans += 1
                k -= num
        return ans
