# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False
        
#       考虑左下角或者右上角的两个点
#       左下角
#         x = len(matrix)-1
#         y = 0
#         while True:
#             if matrix[x][y] == target:
#                 return True
#             elif matrix[x][y] < target:
#                 y = y + 1
#             elif matrix[x][y] > target:
#                 x = x - 1
            
#             if x < 0 or y >= len(matrix[0]):
#                 return False
        
# 第一遍复习写出答案
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        i = m-1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
                
                
