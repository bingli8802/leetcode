class Solution(object):
    # Returns true if all of the items are True (or if the iterable is empty). 
    # All can be thought of as a sequence of AND operations on the provided iterables. 
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        min_len_item = min(A, key = len)
        for char in min_len_item:
            if all(char in i for i in A):
                res.append(char)
                # string.replace(old, new, count)
                A = [i.replace(char, '', 1) for i in A]
        return res
    
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        
        ans = Counter(A[0])
        for i in A[1:]:
            # 对两个计数器交集操作
            ans &= Counter(i)
        # ans = Counter({u'l': 2, u'e': 1})
        return list(ans.elements())
