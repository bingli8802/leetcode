class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        for i in range(n):
            dic1 = dict(collections.Counter(board[i]))
            # print dic1
            for i, v in dic1.items():
                if i.isdigit() and v > 1:
                    return False
        for j in range(n):
            dic2 = dict(collections.Counter([board[i][j] for i in range(n)]))
            # print dic2
            for i, v in dic2.items():
                if i.isdigit() and v > 1:
                    return False     
        for s in range(0, n, 3):
            for t in range(0, n, 3):
                tmp = [board[i][j] for j in range(t, t+3) for i in range(s, s+3)]
                dic3 = dict(collections.Counter(tmp))
                # print dic3
                for i, v in dic3.items():
                    if i.isdigit() and v > 1:
                        return False
        return True     
                    
        
    
