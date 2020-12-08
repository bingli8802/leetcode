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
    # 优化  
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
            print even, odd
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
        return s[start:start + max_len]
    
    # 官方解法dp 
    # 状态转移方程 p(i,j) = p(i+1, j-1) is true and s[i] == s[j]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 k+1
        for k in range(n):
            # 枚举子串的起点 i，可以通过 j=i+k 得到子串的结束位置
            for i in range(n):
                j = i + k
                if j >= n:
                    break
                # 当长度是1 任何一个字母都是回文的
                if k == 0:
                    dp[i][j] = True
                # 当长度是2 只要检查首位两个字母就行
                elif k == 1:
                    dp[i][j] = (s[i] == s[j])
                # 当长度大于2 就要用到状态转移方程
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                # 最后判断如果当前长度大于ans 更新结果
                if dp[i][j] and k + 1 > len(ans):
                    ans = s[i:j+1]
        return ans


