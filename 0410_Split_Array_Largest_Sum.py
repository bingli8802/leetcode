class Solution(object):
    # dp 看不懂
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        f = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i+1, m+1)):
                for k in range(i):
                    max_sum = max(f[k][j - 1], sub[i] - sub[k])
                    f[i][j] = min(f[i][j], max_sum)
            print f
        
        return f[n][m]
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """   
        # [7,2,5,10,8], x = 15
        def check(x):
            total, cnt = 0, 1
            for num in nums:
                # sum([7,2,5]) = 14
                # 14 + 10 > 15 so cnt + 1 becomes 2 and total is 10
                # 10 + 8 > 15 so cnt + 1 becomes 3 and total is 8
                # since cnt is 3 and is greater than m so need to increase leftbound
                # 如果这个加起来的和比上限大，说明要分组了
                # 那么cnt += 1，同时这个数作为新组的开头，即sums = 这个遍历的数
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt

        # [7,2,5,10,8] find a number between 10~33 to make cnt == m
        # mid = 21, cnt = 1 means mid is too large and need to reduce rightbound
        # mid = 15, cnt = 3 means mid is too small and need to increase leftbound
        # 我们给定了mid,如果以mid作为最大值,能形成几组,和给定的m值作对比。如果这个mid越大，要分出来的组数越少。
        # 如果形成的组数比要求的多，说明这个给定的mid太小了，要扩大，而如果形成的组数太少了，说明给定的mid太大了，要缩小。

        left = max(nums) # leftbound = 10
        right = sum(nums) # rightbound = 33
        
        while left < right:
            mid = (left + right) // 2
            if check(mid) <= m:
                right = mid
            else:
                left = mid + 1
        return left

