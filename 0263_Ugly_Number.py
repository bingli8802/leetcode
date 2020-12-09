class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        nums = [2,3,5]
        
        for i in nums:
            # 如果这个数能被2，3，5 整除 就继续整除
            # 当不能整除2，3，5则退出循环
            while num % i == 0:
                num = num / i
        # 如果剩余数字不是1 则这个数一定是其他质数 返回false
        return num == 1

