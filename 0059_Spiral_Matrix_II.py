class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        rs, cs = 0, 0 # 初始行和列
        re, ce = n, n # 终点行和列
        number = 1
        
        while rs < re and cs < ce:
            for i in range(cs, ce): #从第一行开始遍历
                res[rs][i] = number
                number += 1
            rs += 1 #初始行加一 往下移一行
            if rs >= re:
                break
                
            for i in range(rs, re): #从最后一列开始遍历
                res[i][ce-1] = number
                number += 1
            ce -= 1 #终点列减一 往左移一列
            if cs >= ce:
                break
            
            for i in range(ce-1, cs-1, -1):
                res[re-1][i] = number #从最后一行开始遍历
                number += 1
            re -= 1 #终点行减一 往上移一行
            if rs >= re:
                break
            
            for i in range(re-1, rs-1, -1):
                res[i][cs] = number #从第一列开始遍历
                number += 1
            cs += 1 #初始列加一 往右移一列
            if cs >= ce:
                break
        return res
            
            
