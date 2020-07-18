class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        carry = 0
        rem = ""
        
        while n1 >= 0 or n2 >= 0:
            
            left = int(num1[n1]) if n1>=0 else 0
            right = int(num2[n2]) if n2>=0 else 0
            
            tem = left + right + carry
            rem = str(tem%10) + rem
            carry = tem/10
            
            n1 = n1 - 1
            n2 = n2 - 1
        
        if carry == 0:
            return rem
        else:
            return str(carry)+rem
