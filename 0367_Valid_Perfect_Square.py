# 第一遍刷题写
# class Solution(object):
#     def isPerfectSquare(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
        
#         if num <= 1:
#             return True
        
#         left = 1
#         right = num
        
#         while left < right:
#             mid = (left+right+1)/2
#             if mid * mid == num:
#                 return True
#             elif mid * mid > num:
#                     right = mid - 1
#             elif mid * mid < num:
#                     left = mid
#         return False
#
# 第二次看完教程/笔记写
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
#       退出循环条件：
#       left+1大于right 或者right-1小于left 循环结束

        if num <= 1:
            return True
 
        left = 1
        right = num 
        while left <= right:
            mid = (left+right)/2
            if mid * mid == num:
                return True
            # 严格大于 target 的元素一定不是解
            elif mid * mid > num:
                    right = mid - 1
            # 严格小于 target 的元素一定不是解
            elif mid * mid < num:
                    left = mid + 1
        return False

# 第三次看完教程
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
#       退出循环条件：
#       left+1大于right 或者right-1小于left 循环结束
        
        left = 0
        right = num
        
        while left <= right:
            mid = (left+right)/2
            if mid * mid == num:
                return True
            # 严格大于 target 的元素一定不是解
            elif mid * mid > num:
                    right = mid - 1
            # 严格小于 target 的元素一定不是解
            elif mid * mid < num:
                    left = mid + 1
        return False
