class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        print dp
        return dp[n]
    
    # 和第一种解法思路类似 但是更好理解 效率也更高
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # lst is to store all the perfect squares that are smaller or equal to n
        # lst用来存放所有比n小的完全平方数
        lst = [i*i for i in range(1,n) if i*i <= n]
        # create another list dp to store perfect squares that a number need from 1 to n
        # dp存放所有小于n的数 遍历每一个数字
        dp = [0] * (n+1)
        for num in range(1,n+1):
            # number from 1 to 5 
            # for each number, it can be divided into n 1's 
            # 对于每个数字num来说 都可以拆分成num个1 所以把当前最小完全平方数就设为num
            # 比如3 它可以拆分成3个1
            min_num = num
            # a temporary list is to store perfect squares that are smaller or equal to current number
            # 这个临时list存放所有小于3的完全平方数[1]
            tmp_lst = [c for c in lst if c <= num]
            for j in tmp_lst:
                # 在dp中找到num-j的完全平方数的个数 dp[3-1]=1
                perfectSquares = dp[num-j] + 1
                if perfectSquares < min_num:
                    min_num = perfectSquares
            dp[num] = min_num
        return dp[n]

