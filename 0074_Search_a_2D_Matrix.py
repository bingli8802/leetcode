class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        
        left = 0
        right = row * col - 1
        
        while left <= right:
            middle = (left+right)/2
#           巧妙的用了一个方法 计算matrix[r][c]
            r = middle/col
            c = middle%col
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = middle + 1
            elif matrix[r][c] > target:
                right = middle - 1
        return False
