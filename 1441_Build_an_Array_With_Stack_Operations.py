class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        li = [i for i in range(1,n+1)]
        j = 0
        res = []
        while j < len(target):
            if target[j] == li[j]:
                res.append("Push")
                j += 1
            else:
                res.append("Push")
                res.append("Pop")
                li.pop(j)      
        return res
