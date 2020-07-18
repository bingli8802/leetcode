class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        last = len(digits)-1
        
        while last >= 0:
            if digits[last] == 9:
                digits[last] = 0
                carry = 1
                last = last - 1
            else: 
                digits[last] = digits[last] + 1
                carry = 0
                break 
                
        if carry == 0:
            return digits
        else:
            digits.insert(0,1)
            return digits
