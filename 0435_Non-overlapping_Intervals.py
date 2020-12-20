class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        n = len(intervals)
        # 先排序 按照第二元素升序排序
        intervals.sort(key = lambda x: x[1])
        # print intervals
        end = intervals[0][1]
        cnt = 1
        for interval in intervals:
            start = interval[0]
            if start >= end:
                cnt += 1
                end = interval[1]    
        return n - cnt
