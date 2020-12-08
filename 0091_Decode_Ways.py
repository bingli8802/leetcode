class Solution(object):
    # 网上答案
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': 
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1 # 假设没有先导0
        for i in range(1, len(s)):
            # 如果当前位置是0 它前一个不是1和2 直接返回0
            if s[i]=='0' and s[i-1] not in ['1','2']: 
                return 0  
            elif s[i]=='0':
                dp[i] = dp[i-2] if i>1 else 1
            elif 11 <= int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i-1]+dp[i-2] if i>1 else dp[i-1]+1
            else:
                dp[i] = dp[i-1]
        return dp[-1]
    
    # 代码重新排版
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': 
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1 # 假设没有先导0
        for i in range(1, len(s)):
            # 如果当前数是0 它前一个数不是1和2 直接返回0 “4012”
            if s[i]=='0' and s[i-1] not in ['1','2']: 
                return 0  
            # 如果当前数是0 
            elif s[i]=='0':
                # 如果0在第二个位置上 只有一种情况 “1023”
                if i == 1:
                    dp[i] = 1
                # 如果0不在第二个位置上 返回第i-2个位置上的组合数“1120”
                else:
                    dp[i] = dp[i-2]
            # 如果当前位置不是0 它前一个数字组成的数字当前数字范围在(11,26)之间
            elif 11 <= int(s[i-1:i+1]) <= 26:
                # 如果当前在第二个位置上 返回位置0上的组合数加一 “1” - “2134”
                if i == 1:
                    dp[i] = dp[0] + 1
                # 如果当前不在第二个位置上 返回前两个位置上组合数的和 “3” - “2134”
                else:
                    dp[i] = dp[i-1]+dp[i-2]
            # 如果当前位置不是0 他和前一个数字组成的数字范围 < 11 "3" - "103"
            else:
                dp[i] = dp[i-1]
        return dp[-1]

