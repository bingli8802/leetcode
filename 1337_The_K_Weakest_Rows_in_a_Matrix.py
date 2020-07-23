class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        row = len(mat)
        col = len(mat[0])
        
        for r in range(0, row):
            left = 0
            right = col
#           找最左边0的index 并记录下来 这就是1的个数
            while left < right:
                middle = (left+right)/2
                if mat[r][middle] == 0:
                    right = middle
                elif mat[r][middle] == 1:
                    left = middle + 1
#           把 [行的index，士兵的个数] 放到ret 再进行比较
            ret.append([r,right])
    
#       lambda函数
        ret.sort(key=lambda x: (x[1], x[0]))
        return [i[0] for i in ret[:k]] 

