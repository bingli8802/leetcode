class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = [[r0, c0]]
        step, direction = 1, 1
        row, col = r0, c0
        
        while len(res) < R * C:
            # walk rightwards or leftwards
            for _ in range(step):
                col += direction
                if 0 <= row < R and 0 <= col < C:
                    res.append([row, col])
                    
            # walk downwards or upwards      
            for _ in range(step):
                row += direction
                if 0 <= row < R and 0 <= col < C:
                    res.append([row, col])
                    
            # increase step by one each time and change the direction
            step += 1
            direction *= -1
        return res
            
            
