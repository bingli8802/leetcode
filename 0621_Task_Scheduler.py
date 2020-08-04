class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        
        # 计算每个任务的个数 比如：Counter({u'A': 3, u'B': 3, u'C': 1})
        count = Counter(tasks)

        # 计算有几个任务 -> 4
        cnt = len(count)

        # 找到同一任务出现的最大次数 -> 3
        max_cnt = max(count.values())

        # 找到有几个任务同时出现最大次数3 -> 2
        max_cnt_tasks = Counter(count.values()).get(max_cnt)
        
        # 计算
        res = (max_cnt - 1) * (n + 1) + max_cnt_tasks
        
        # 如果间隔数小于任务数，则返回数组长度
        # 如果间隔数大于等于任务数，则计算结果：(max(相同类出现的次数)-1)*(n+1) + 相同类出现次数最多的类数量
        if n < cnt:
            return max(len(tasks), res)
        else:
            return res
