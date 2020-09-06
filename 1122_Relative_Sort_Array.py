class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # counter 计数器
        from collections import Counter
        c = Counter(arr1)
        hashmap = dict(c)
        res = []
        for i in arr2:
            for j in range(hashmap.get(i)):
                res.append(i)
        diff = [item for item in arr1 if item not in arr2]
        return res + sorted(diff)
    
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # defaultdict
        from collections import defaultdict
        dic = defaultdict(int)
        for k, v in enumerate(arr2):
            dic[v] = k
        li = [[] for i in range(len(arr2) + 1)]
        for num in arr1:
            index = dic.get(num)
            if index is not None:
                li[index].append(num)
            else:
                li[-1].append(num)
        li[-1].sort()
        # flatten a list
        return [x for sublist in li for x in sublist]
    
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res1=[]
        res2=[]
        for x in arr1:
            if x not in arr2:
                res1.append(x)
            else:
                res2.append(x)
        # lambda function
        res2.sort(key=lambda x: arr2.index(x))
        return res2+sorted(res1)

