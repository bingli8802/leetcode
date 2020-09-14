class Solution(object):
    # 自己解法超时
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        for i in range(1, len(A)-1):
            if all(A[m] > A[m-1] for m in range(1, i+1)) and all(A[n] > A[n+1] for n in range(i, len(A)-1)):
                return True
        return False
    # 改进
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        if A[-1] > A[-2] or A[0] > A[1]:
            return False
        flag = "grt"
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                flag = "sml"
            if A[i] >= A[i+1] and flag == "grt" or A[i] <= A[i+1] and flag == "sml":
                return False         

        return True
    # 官方解法
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        i = 0
        # walk up
        while i < N-1 and A[i] < A[i+1]:
            i += 1
        # peak can't be first or last
        if i == 0 or i == N-1:
            return False
        # walk down
        while i < N-1 and A[i] > A[i+1]:
            i += 1
        return i == N-1
