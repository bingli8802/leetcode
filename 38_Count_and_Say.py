class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        previous = ''
        
        if n == 1:
            return '1'
        
        previous = self.countAndSay(n-1)
        count = 1
        
        if len(previous) == 1:
            return str(count) + previous
        
        ret = ''
        
        for i in range(len(previous)-1):
            left = previous[i]
            right = previous[i+1]

            if left != right:
                ret += str(count)+left
                count = 1
                
            elif left == right:
                count +=1  
        ret += str(count) + previous[-1]
        return ret

