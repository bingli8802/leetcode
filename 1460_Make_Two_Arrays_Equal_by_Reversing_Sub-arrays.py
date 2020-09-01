class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        # return sorted(target) == sorted(arr)
        target.sort()
        arr.sort()
        return target == arr
