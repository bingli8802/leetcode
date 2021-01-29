class Solution(object):
    # based on a pattern
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """ 
        pos1,pos2 = 0,len(matrix)-1
        while pos1 < pos2:
            add = 0
            while add < pos2-pos1:
                matrix[pos1][pos1+add], matrix[pos1+add][pos2], matrix[pos2][pos2-add], matrix[pos2-add][pos1] = \
                matrix[pos2-add][pos1], matrix[pos1][pos1+add], matrix[pos1+add][pos2], matrix[pos2][pos2-add]
                add = add+1
            pos1 = pos1+1
            pos2 = pos2-1

    # reverse the whole matrix
    # then flip the image diagonal
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """ 
        matrix[:] = matrix[::-1]
        print matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
        
