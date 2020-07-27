# 第一种做法 改变list
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

# 第二种做法 双指针 不改变list
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        li = [x for x in range(1,n+1)]
        i = 0
        j = 0
        res = []
        while i < len(target):
            while j < len(li):
                if target[i] == li[j]:
                    res.append("Push")
                    i += 1
                    j += 1
                    break
                else:
                    res.append("Push")
                    res.append("Pop")
                    j += 1         
        return res
                
