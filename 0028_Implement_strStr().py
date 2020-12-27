class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        h,n = len(haystack),len(needle)
        
        if n == "":
            return 0
        
        else:
            for i in range(h-n+1):
                if needle == haystack[i:i+n]:
                    return i
            return -1
            
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 空needle返回0
        if needle == '':
            return 0
        
        # KMP()函数返回列表dp，dp是一个状态转移图，dp的构成只与needle有关
        def KMP():
            M = len(needle)
            # dp是一个长度与needle长度相等的二维list,状态的数量与needle长度是相同的
            dp = [[0] * 101 for _ in range(M)]
            # 初始化状态0，只有needle[0]对应的字符才能使状态转移
            dp[0][ord(needle[0])] = 1
            # 初始化影子状态x
            x = 0
            # 对于每个状态...
            for j in range(1,M):
                # 对于每种字符(ASCII码的0~255)
                for c in range(101):
                    # 第j个状态对于除needle[j]对应的字符以外的新字符输入的响应,与影子变量的响应相同
                    dp[j][c] = dp[x][c]
                # 遇到needle[j]，则进入下一状态
                dp[j][ord(needle[j])] = j + 1
                # 更新影子状态x，更新为当前x遇到needle[j]后转移到的状态
                x = dp[x][ord(needle[j])]
            return dp

        dp = KMP()
        print dp
        # dp初始化完毕，下面为查找部分代码
        M = len(needle)
        N = len(haystack)
        # 初始化当前状态为0
        j = 0
        # 对于haystack中的每个字符...
        for i in range(0, N):
            # 对输入字符haystack[i]的状态转移
            j = dp[j][ord(haystack[i])]

            # j == n则匹配上了，返回匹配位置
            if j == M:
                return i - M + 1

        # 未匹配上返回-1
        return -1
