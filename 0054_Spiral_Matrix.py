class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rs, cs = 0, 0       # 设置行的起始位置rs=0和列的起始位置cs=0
        re, ce = len(matrix), len(matrix[0])    # 设置行的结束位置re=n和列的结束位置ce=n
        res = []    # 存放结果的数组
        while rs < re and cs < ce:
            for i in range(cs,ce):            # 遍历首行
                res.append(matrix[rs][i])
            rs += 1
            if rs>=re:
                break
            
            for j in range(rs,re):            # 遍历尾列
                res.append(matrix[j][ce-1])
            ce -= 1
            if cs>=ce:
                break
            
            for i in range(ce-1,cs-1,-1):     # 遍历尾行
                res.append(matrix[re-1][i])
            re -= 1
            if rs>=re:
                break
            
            for j in range(re-1,rs-1,-1):     # 遍历首列
                res.append(matrix[j][cs])
            cs += 1
            if cs>=ce:
                break
        return res
