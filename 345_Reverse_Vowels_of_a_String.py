class Solution(object):
    def reverseVowels(self, a):
        """
        :type s: str
        :rtype: str
        """
        
        li = 'aeiouAEIOU'
        s = list(a) 
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] in li:
                if s[j] in li:
                    s[i], s[j] = s[j], s[i]
                    j = j - 1
                    i = i + 1
                else:
                    j = j - 1
            else:
                i = i + 1
        return ''.join(s)

#         vowel_str = ['a','e','i','o','u','A','E','I','O','U']
#         li = list(a) 
#         idx_li = []
        
#         for i,v in enumerate(li):
#             if v in vowel_str:
#                 idx_li.append(i)
        
#         mid = int(len(idx_li)/2)
        
#         for j in xrange(0,mid):
        
#             li[idx_li[j]], li[idx_li[len(idx_li)-1-j]] = li[idx_li[len(idx_li)-1-j]], li[idx_li[j]]
            
#         return ''.join(li)
        
