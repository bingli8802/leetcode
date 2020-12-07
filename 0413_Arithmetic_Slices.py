class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        diff = A[0] - A[1]
        cnt = 1
        dp = []
        res = 0     
        for i in range(1, n-1):
            curDiff = A[i] - A[i+1]
            if curDiff != diff:
                diff = curDiff
                dp.append(cnt)
                cnt = 1  
            else:
                cnt += 1
        dp.append(cnt)    
        for k in dp:
            if k >=2:
                res += k*(k-1)/2
        return res
        
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n <3:
            return 0
        dp = [0]*n
        sum = 0
        for i in range(2,n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
                sum += dp[i]
        print dp
        return sum

