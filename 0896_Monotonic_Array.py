class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = ""
        if len(A) == 1:
            return True
        if A[0] < A[1]:
            flag = "Small"
        elif A[0] > A[1]:
            flag = "Large"
        else:
            flag = "Equal"
        for i in range(1, len(A)-1):
            if A[i] < A[i+1]:
                if flag == "Large":
                    return False
                flag = "Small"
            elif A[i] > A[i+1]:
                if flag == "Small":
                    return False
                flag = "Large"
        return True
    
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return (all(A[i] <= A[i+1] for i in xrange(len(A) - 1)) or 
                all(A[i] >= A[i+1] for i in xrange(len(A) - 1)))


