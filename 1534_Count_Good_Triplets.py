class Solution(object):
    # O(n^3)
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1
        return ans
    # 递归优化 循环提前结束
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, len(arr)):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) <= c:
                        ans += 1
        return ans
