class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        board = board[0]+board[1]  # 把board连起来变一维
        # print board
        neighbors = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]  # 每个位置的0可以交换的位置
        # q = [(state, now, step), (state, now, step),...]
        q = [(tuple(board), board.index(0), 0)]
        # print q
        visited = set()  # bfs队列和已访问状态记录
        
        while q:
            state, now, step = q.pop(0)  # 分别代表当前状态，0的当前位置和当前步数
            if state == (1, 2, 3, 4, 5, 0):  # 找到了
                return step
            for neignbor in neighbors[now]:  # 遍历所有可交换位置
                cur = list(state)
                cur[neignbor], cur[now] = cur[now], cur[neignbor]  # 交换位置
                cur = tuple(cur)
                if cur not in visited:  # 确认未访问
                    q.append((cur, neignbor, step+1))
            visited.add(state)
        return -1


