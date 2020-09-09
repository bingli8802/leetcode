class Solution(object):
    # Counter
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = -1
        c = collections.Counter(arr)
        for i in c:
            if c[i] == i:
                res = max(res, i)
        return res
    # defaultdict
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = -1
        dic = collections.defaultdict(int)
        for i in arr:
            dic[i] += 1
        for k in dic.keys():
            if dic[k] == k and k > res:
                res = k
        return res
    
    # dictionary
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = -1
        dic = {}
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
        for k in dic.keys():
            if dic[k] == k and k > res:
                res = k
        return res
