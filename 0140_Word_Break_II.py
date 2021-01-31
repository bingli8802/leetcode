class Solution(object):
    # 自己解法超时
    # 回溯
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        def back(curr, rem):
            if len(rem) == 0:
                res.append(curr[1:])
                return
            for i in range(len(rem)):
                if rem[:i+1] in wordDict:    
                    back(curr+' '+rem[:i+1], rem[i+1:])
        back('', s)
        return res
    
    # 回溯加memo
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        memo = [1] * (len(s)+1)
        def search(string, idx):
            tmp = len(res)
            if idx == len(s): 
                res.append(string)
                return
            if idx > len(s): 
                return None
            for word in wordDict:
                if memo[idx] and word == s[idx:idx+len(word)]:
                    if len(string):
                        search(string+" "+word, idx+len(word))
                    else:
                        search(word, len(word))
            memo[idx] = 1 if len(res)>tmp else 0
        search("", 0)
        return res
    

    
