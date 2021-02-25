class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        '''
        [4,10,15,24,26]
         i
        [0,9,12,20]
         j
        [5,18,22,30]]
         k
        '''        
        k = len(nums)
        if k==1: 
            return [nums[0][0],nums[0][0]]
        indexs = [0] * k
        lists = []
        largest = -float('inf')
        import heapq
        # 生成大小为k的堆
        for i in range(k):
            num = nums[i][0]
            heapq.heappush(lists,(num,i))
            largest = max(largest,num)
            # print lists [(0, 1), (4, 0), (5, 2)]

        #lists[0][0] is the smallest element in the heap(lists)
        left,right = lists[0][0],largest

        while True:
            num,i = heapq.heappop(lists)
            # 取出最小的数，以及对应的列表的下标
            indexs[i] += 1
            # 下标+1
            if indexs[i] >= len(nums[i]): # 退出循环
                break
            # 通过下标i找到列表，再通过indexs数组找到下一个元素的下标
            newnum = nums[i][indexs[i]]
            heapq.heappush(lists,(newnum,i)) #插入新的数
            largest = max(largest,newnum) # 更新最大值
            if largest-lists[0][0] < right - left: #更新区间
                left, right = lists[0][0], largest
        return [left,right]

        
