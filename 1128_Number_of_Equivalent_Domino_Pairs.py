class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        ans = 0
        d = collections.defaultdict(int)
        for i, j in dominoes:
            num = 10 * i + j if i < j else 10 * j + i
            d[num] += 1
        for v in d.values():
            ans += v * (v - 1) / 2
        return ans
