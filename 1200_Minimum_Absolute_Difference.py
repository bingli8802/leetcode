class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # arr = sorted(arr)
        # arr[:] = sorted(arr)
        arr.sort()
        min_diff = abs(arr[0] - arr[1])
        res = [[arr[0], arr[1]]]
        for i in range(1, len(arr) - 1):
            diff = abs(arr[i] - arr[i+1])
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                res.append([arr[i], arr[i+1]])
        return res
