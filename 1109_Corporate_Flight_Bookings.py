class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # a就相当于diff数组
        a = [0]*(n+1)   # n+1个航班，+1是为了方便计算（处理边界）
        # 给diff做加减操作
        for i,j,k in bookings:
            a[i-1] += k
            a[j] -= k
        # 根据diff反推原始数组
        for i in range(n):
            a[i+1] += a[i]
        return a[:-1]

