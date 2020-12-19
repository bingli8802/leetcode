class Solution(object):
    # 自己解法超时
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""  
        def isPalindrome(sub):
            m = len(sub)
            for i in range(m/2):
                if sub[i] != sub[m-1-i]:
                    return False
            return True             
        res = ""
        n = len(s)
        for i in range(n):
            for j in range(n, i, -1):
                if isPalindrome(s[i:j]):
                    if j-i+1 > len(res): 
                        res = s[i:j]
        return res
    
    # 二维dp 不超时 但是比较慢
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = ""
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i - j < 2 or dp[i-1][j+1] == 1):
                    dp[i][j] = 1
                    if len(s[j:i+1]) > len(res):
                        res = s[j:i+1]
        return res
    
    # 优化 中心扩展法 不超时
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        res = s[0]
        def extend(i, j, s):
            while(i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            return s[i + 1:j]

        for i in range(n-1):
            e1 = extend(i, i, s)
            e2 = extend(i, i + 1, s) 
            if max(len(e1), len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2
        return res
    
    # 最优解
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: 
            return ""
        n = len(s)
        if n == 1 or s == s[::-1]: 
            return s
        max_len,start = 1,0
        for i in range(1, n):
            even = s[i-max_len:i+1]
            odd = s[i-max_len-1:i+1]
            # print even, odd
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
        return s[start:start + max_len]
    

    



