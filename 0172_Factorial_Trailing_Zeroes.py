class Solution(object):
    # 末尾唯一的零来自于 2 * 5。很显然，如果需要产生零，阶乘中的数需要包含 2 和 5 这两个因子。
    # 例如：4 * 10 = 40 也会产生零，因为 4 * 10 = ( 2 * 2 ) * ( 2 * 5) 。
    # 因此，我们只要数一数组成阶乘的数中共有多少对 2 和 5 的组合即可。又因为 5 的个数一定比 2 少，问题简化为计算 5 的个数就可以了。
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0   
        while n >= 5:
            res += n // 5
            n //= 5        
        return res

