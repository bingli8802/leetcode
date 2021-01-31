class Solution(object):
    # minHeap 用内置函数维护一个最小堆
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """        
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        res = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        
        return res
    
    # deque双端队列
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        n = len(nums)
        if n == 0:
            return []
        res = []
        # 滑动窗口，注意：保存的是索引值
        window = deque()

        for i in range(n):
            # 当左边界到当前位置距离等于k，那么将它弹出
            if i >= k and i - k == window[0]:
                window.popleft()
            # 如果滑动窗口非空，新进来的数比前一个数（也就是队尾的数）要大，pop队尾
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            # 入队    
            window.append(i)
            
            # 队首一定是滑动窗口的最大值的索引
            if i >= k - 1:
                res.append(nums[window[0]])
        return res

