class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
#       思路
#       遍历grid每一行，找到第一负数，那么之后都是负数
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for i in range(m):
            left = 0
            right = n
            while left < right:
                mid = (left+right)/2
                if grid[i][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid
            cnt += n-right
        return cnt
                
            
