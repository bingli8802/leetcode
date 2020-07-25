"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""

class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
#       思路
#       初始化x=1，用二分法找y
        x=1
        ret = []
#       x可能取到的值应该是[1,z]
        for x in range (1,z+1):
            left = 1
#           right可以写成 right=z，但是每次x增加后，y的取值范围应该缩小
#           right=z
            right = z-x+1
            while left <= right:
                mid = (left+right)/2
#               如果找到等于z的一对(x,y) 跳出循环体
                if customfunction.f(x,mid) == z:
                    ret.append([x,mid])
                    break
                elif customfunction.f(x,mid) < z:
                    left = mid + 1
                elif customfunction.f(x,mid) > z:
                    right = right - 1
        return ret
