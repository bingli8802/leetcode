class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        from collections import Counter
        res = 0
        d = dict(Counter(chars))
        for word in words:
            cnt = dict(Counter(word))
            if all(d.get(k) is not None and d.get(k) >= cnt.get(k) for k in cnt.keys()):      
                res += len(word)
        return res
    
    # 不把counter转换成dict也可以
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        from collections import Counter
        res = 0
        d = Counter(chars)
        for word in words:
            cnt = Counter(word)
            if all(d[k] is not None and d[k] >= cnt[k] for k in cnt):      
                res += len(word)
        return res
    
    # 官方解法
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans


