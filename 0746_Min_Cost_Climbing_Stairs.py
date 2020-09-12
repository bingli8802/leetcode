class Solution(object):
    # 原地修改原来数组
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
        return min(cost[-2], cost[-1])
    # 使用额外数组 效率低一些
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        li = [0] * len(cost)
        li[0] = cost[0]
        li[1] = cost[1]
        for i in range(2, len(cost)):
            li[i] = min(li[i-2], li[i-1]) + cost[i]
        return min(li[-2], li[-1])
