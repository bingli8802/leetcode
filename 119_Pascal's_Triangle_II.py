class Solution(object):
    # 递归
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex-1)
        return [1] + [prev[i] + prev[i+1] for i in range(rowIndex-1)] + [1]
    
    # 迭代
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] 
        for row_num in range(1, rowIndex+1):
            # 先把row1计算出来 再计算row2 row3 。。。
            temp = [None for _ in range(row_num+1)]
            temp[0], temp[-1] = 1, 1
    
            for i in range(1, row_num):
                temp[i] = row[i-1] + row[i]
            # row变成row1的值
            row = temp
        return row
            
