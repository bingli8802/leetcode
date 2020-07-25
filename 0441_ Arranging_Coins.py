class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """  
#       返回 x*(x+1)/2 <= n 最大x的值
        left = 0
        right = n
        while left < right:
#           如果选择左边界不能排除中位数，则中位数应该取右中位数            
            mid =  (left + right + 1)/2
            if mid*(mid+1)/2 == n:
                return mid
#           严格大于n 则x一定不是 区间就是[left,mid-1]
            elif mid*(mid+1)/2 > n:
                right = mid - 1
#           小于n,则mid有可能就是目标值，区间应该是[mid, right]
            else: 
#         如果选择左边界不能排除中位数，则中位数应该取右中位数
                left = mid 
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

