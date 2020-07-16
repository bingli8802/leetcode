class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = len(a)-1
        n2 = len(b)-1
        carry = 0
        ret = ""
        
        while n1>=0 or n2>=0:
            left = int(a[n1]) if n1>=0 else 0
            right = int(b[n2]) if n2>=0 else 0
            
            if left!= right:
                if carry == 0:
                    ret = "1"+ ret 
                else:
                    ret = "0" + ret

            elif left == right:
                ret = str(carry) + ret
                carry = 1 if left == 1 else 0
                
            n1 = n1-1
            n2 = n2-1 
            
        if carry == 0:
            return ret 
        else:
            return str(carry) + ret
