    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        a = sorted(set(arr))
        dic = collections.defaultdict(int)
        for k, v in enumerate(a):
            dic[v] = k + 1
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return arr
