class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # 定义一个返回变量 长度为n
        res = [0]*n
        stack = []
        time_s = []
        for log in logs:
            id, flag, time = log.split(":")
            # 如果是start 就把id和时间分别入栈
            if flag == "start":
                stack.append(int(id))
                time_s.append(int(time))
            # 如果是end 就计算interval 并把stack，time_s分别出栈
            elif flag == "end":
                interval = int(time) - time_s.pop() + 1
                # 把时间加在相应id那里
                res[stack.pop()] += interval
                # 如果stack不为空，栈顶元素的time应该减掉interval
                if len(stack) != 0:
                    res[stack[-1]] -= interval
        return res
    
