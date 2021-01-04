class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = res = 0
        window = collections.defaultdict(int)
        
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            
            # 收缩左边界 直到window[c]==1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left)
        return res


