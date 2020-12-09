class Solution(object):
    # 网上答案 回溯
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        state=[]
        def back(state,s):
            if len(s)==0:
                res.append(state)
                return
            for i in range(len(s)):
                temp=s[:i+1]
                if temp==temp[::-1]:
                    back(state+[temp],s[i+1:])
        back(state,s)
        return res
    # 推导过程 
    # back([], "aabc")
    # ->temp = a, back([a], "abc")
    #             ->temp = a, back([a,a], "bc")
    #                         ->temp = b, back([a,a,b], "c")
    #                                     ->temp = c, back([a,a,b,c], "")
    #                                     ->res = [[a,a,b,c]]
    #                         ->temp = bc
    #             ->temp = ab
    #             ->temp = abc
    # ->temp = aa, back([aa], "abc")
    #             ->temp = b, back([aa,b], "c")
    #                         ->temp = c, back([aa,b,c],"")
    #                         ->res = [[a,a,b,c],[aa,b,c]]
    # ->temp = aab
    # ->temp = aabc
