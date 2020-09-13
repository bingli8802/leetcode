class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # 计算斜率
        # 为了消除分母为零的影响，该为乘积方式，乘积不为0，返回false
        if len(coordinates) == 2:
            return True
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        
        for i in range(2, len(coordinates)):
            x3, y3 = coordinates[i][0], coordinates[i][1]
            if (y3 - y2)*(x2 - x1) != (y2 - y1)*(x3 - x2):
                return False
        return True

