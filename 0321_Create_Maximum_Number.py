class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # find max number of length m
        def pick_max(nums, m):
            stack = []
            rem = len(nums) - m
            for num in nums:
                while rem and stack and stack[-1] < num:
                    stack.pop()
                    rem -= 1
                stack.append(num)
            return stack[:m]

        # merge two list
        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        # i从0开始递归
        res = []
        for i in range(k+1):
            if i > len(nums1) or k-i > len(nums2):
                continue
            arr1 = pick_max(nums1, i)
            arr2 = pick_max(nums2, k-i)
            print i, arr1, arr2
            res = max(res, merge(arr1, arr2))
        return res

            # return max(merge(pick_max(nums1, i), pick_max(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))

