class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        '''
         2    3
        /|\
       a b c
      /|\
     d e f
        '''
        def backTrack(i, tmp):
            if i == n:
                output.append(tmp)
                return
            # print dic[digits[i]]
            for letter in dic[digits[i]]:
                backTrack(i+1, tmp+letter)
                    
        
        dic = {'2':['a','b','c'], 
               '3':['d','e','f'], 
               '4':['g','h','i'], 
               '5':['j','k','l'], 
               '6':['m','n','o'], 
               '7':['p','q','r','s'], 
               '8':['t','u','v'], 
               '9':['w','x','y','z']}
        
        if not digits:
            return  []
        output = []
        n = len(digits)
        backTrack(0,'')
        return output
