class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # 每个位置上加一的操作
        def plusOne(s, j):
            ch = [i for i in s]
            if ch[j] == '9':
                ch[j] = '0'
            else:
                ch[j] = str(int(ch[j]) + 1)
            return ''.join(ch)
        # 每个位置上减一的操作
        def minusOne(s, j):
            ch = [i for i in s]
            if ch[j] == '0':
                ch[j] = '9'
            else:
                ch[j] = str(int(ch[j]) - 1)
            return ''.join(ch)
        # bfs
        queue = ['0000']
        visited = {'0000'}
        step = 0
        while queue:
            len_ = len(queue)
            # 将当前队列中所有节点向四周扩散
            for i in range(len_):
                cur = queue.pop(0)
                if cur == target:
                    return step
                if cur in deadends:
                    continue

                # 对每一位进行前一个以及下一个位置的旋转
                for j in range(4):
                    up = plusOne(cur, j)
                    if up not in visited:
                        visited.add(up)
                        queue.append(up)
                    
                    down = minusOne(cur, j)
                    if down not in visited:
                        visited.add(down)
                        queue.append(down)
            step += 1
        return -1

