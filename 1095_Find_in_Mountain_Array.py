# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    # 花花酱
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        def binary_search(left, right, cond):
            while left < right:
                mid = left + (right - left) / 2
                if cond(mid):
                    right = mid
                else:
                    left = mid + 1
            return left
        
        n = mountain_arr.length()
        peak = binary_search(0, n-1, lambda i: mountain_arr.get(i) > mountain_arr.get(i+1))
        
        left = binary_search(0, peak, lambda i: mountain_arr.get(i) >= target)
        if mountain_arr.get(left) == target:
            return left
        
        right = binary_search(peak, n-1, lambda i: mountain_arr.get(i) <= target)
        if mountain_arr.get(right) == target:
            return right
        return -1

    # 拆分成三个binary search
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        def findPeak(left, right):
            while left < right:
                mid = left + (right - left) / 2
                if mountain_arr.get(mid) >= mountain_arr.get(mid+1):
                    right = mid
                elif mountain_arr.get(mid) < mountain_arr.get(mid+1):
                    left = mid + 1
            return left
        
        def searchLeft(left, right):
            while left <= right:
                mid = left + (right - left) / 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) < target:
                    left = mid + 1
                elif mountain_arr.get(mid) > target:
                    right = mid - 1
            return -1
                
        def searchRight(left, right):
            while left <= right:
                mid = left + (right - left) / 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) < target:
                    right = mid - 1
                elif mountain_arr.get(mid) > target:
                    left = mid + 1
            return -1
        
        n = mountain_arr.length()
        peak = findPeak(0, n-1)
        
        left = searchLeft(0, peak)
        if left != -1:
            return left
        else:
            return searchRight(peak, n-1)
