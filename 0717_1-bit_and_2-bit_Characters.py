class Solution(object):
    # 自己解法
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if bits[i] == 0 and i != len(bits) - 1:
                i += 1
            elif bits[i] == 0 and i == len(bits) - 1:
                return True
            elif bits[i] == 1:
                i += 2
        return False
    
    # 官方解法快很多
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits) - 1
        i = 0
        while i < n:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n

