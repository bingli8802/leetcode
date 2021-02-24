class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        flag = -1
        row = 0
        res = [[] for i in range(numRows)]
        
        for c in s:
            res[row].append(c)
            if row == 0 or row == numRows - 1:
                flag *= -1
            row += flag
        
        for i in range(numRows):
            res[i] = ''.join(res[i])
        return ''.join(res)
          
        
