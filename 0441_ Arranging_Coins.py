class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """  
#       返回第一个小于x*(x+1)/2<=n 的x
        # if n == 0:
        #     return 0
        
        left = 0
        # left = 1
        right = n
        
        while left < right:
#         如果选择左边界不能排除中位数，则中位数应该取右中位数            
            target =  (left + right + 1)/2
    
            if target*(target+1)/2 == n:
                return target
#           严格大于n 则x一定不是 区间就是[left,target-1]
            elif target*(target+1)/2 > n:
                right = target - 1
#           小于n 则x有可能就是 区间应该是[target, right]
            elif target*(target+1)/2 < n: 
#         如果选择左边界不能排除中位数，则中位数应该取右中位数
                left = target 
        return left
    
        # while left <= right:
        #     target =  (left + right + 1)/2
        #     if target*(target+1)/2 == n:
        #         return target
        #     elif target*(target+1)/2 > n:
        #         right = target - 1
        #     elif target*(target+1)/2 < n: 
        #         left = target + 1
        # return right

