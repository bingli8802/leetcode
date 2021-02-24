class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        '''
        25525511135
         /  |  \
        2  25  255
       / | \
      5 55 552
     /|\
    5
    /|\
    2
        '''
        def backTrack(s, tmp, cnt):
            if tmp and int(tmp[-1]) > 255:
                return
            elif tmp and len(tmp[-1]) > 1 and tmp[-1].startswith('0'):
                return
            elif cnt == 4 and len(s) > 0:
                return  
            elif len(tmp) == 4:
                output.append('.'.join(tmp))
                # print output
            
            n = 3
            if len(s) < n:
                n = len(s)
            for i in range(n):
                backTrack(s[i+1:], tmp+[s[:i+1]], cnt+1)
        
        if len(s) < 4 or len(s) > 3 * 4:
            return 
        
        output = []
        backTrack(s, [], 0)
        return output
