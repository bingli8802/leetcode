class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        one = []
        res = 1
        for i in range(n):
            if seats[i] == 1:
                one.append(i)
        m = len(one)
        for j in range(1, m):
            temp = (one[j] - one[j-1]) / 2
            # res = max(temp, res)
            if temp>res:
                res=temp
        # 三种情况
        # [1,0,0,0] one[0] = 0, res = 1, n-one[-1]-1 = 3
        # [0,0,0,1] one[0] = 3, res = 1, n-one[-1]-1 = 0
        # [1,0,0,0,1,0,1] one[0] = 0, res = 2, n-one[-1]-1 = 0
        return max(one[0], res, n-one[-1]-1)
  

