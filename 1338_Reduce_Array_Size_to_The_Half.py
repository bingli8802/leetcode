class Solution(object):
    # 自己解法
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = collections.Counter(arr)
        print cnt
        occur = 0
        res = 0
        for i in cnt.most_common():
            if occur * 2 >= len(arr):
                return res
            else:
                occur += i[1]
                res += 1
        return res
    # 官方解法 
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = collections.Counter(arr)
        cnt, ans = 0, 0
        for num, occ in freq.most_common():
            cnt += occ
            ans += 1
            if cnt * 2 >= len(arr):
                break
        return ans

