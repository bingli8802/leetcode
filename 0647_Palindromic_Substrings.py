class Solution(object):
    # 二维dp
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i - j < 2 or dp[i-1][j+1] == 1):
                    # if j - i < 2 or dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    res += 1
        # print dp
        return res
    
    # 中心扩展法 不太理解
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """          
        n = len(s)
        res = 0    
        for i in range(2 * n - 1):
            # left和right指针和中心点的关系是？
            # 首先是left，有一个很明显的2倍关系的存在，其次是right，可能和left指向同一个（偶数时），也可能往后移动一个（奇数）
            left = i / 2
            right = left + i % 2
            print i, left, right, res
            while (left >= 0 and right < n and s[left] == s[right]):
                res += 1
                left -= 1
                right += 1
        return res
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(s,l,r):
            num = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                num += 1
            return num
        
        num = 0
        for i in range(len(s)):
            num += check(s, i, i)
            if i == len(s) - 1:
                continue
            num += check(s, i, i+1)
        return num


