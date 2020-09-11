class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        amount = sum(A)
        if amount % 3 != 0:
            return False
        res = amount // 3
        temp, count = 0, 0
        for i in A:
            if count == 2:
                return True
            temp += i
            if temp == res:
                count += 1
                temp = 0
        # return False

