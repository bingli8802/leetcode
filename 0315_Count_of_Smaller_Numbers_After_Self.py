class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        res = [0] * n
        indexes = []
        
        for index, value in enumerate(nums):
            indexes += [(index, value)]
        
        def merge(tuples):
            if len(tuples) == 1:
                return tuples
            
            mid = len(tuples)//2
            left = merge(tuples[0:mid])
            right = merge(tuples[mid:len(tuples)])
        
            tmp = []
            right_added = 0
            i, j = 0, 0
            
            while i < len(left) and j < len(right):
                if left[i][1] > right[j][1]:
                    tmp += [right[j]]
                    right_added += 1
                    j += 1
                else:
                    tmp += [left[i]]
                    res[left[i][0]] += right_added
                    i += 1                     
            while i != len(left):
                tmp += [left[i]]
                res[left[i][0]] += right_added
                i += 1         
            # tmp += right[j:]
            while j != len(right):
                tmp += [right[j]]
                j += 1
            return tmp
    
        merge(indexes)
        return res
    

