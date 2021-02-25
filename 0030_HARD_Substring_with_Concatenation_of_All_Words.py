class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j+one_word])
            if Counter(c_tmp) == words:
                res.append(i)
        return res

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dic = dict(collections.Counter(words))

        len_of_each_word = len(words[0])
        len_of_words = len_of_each_word * len(words)
        len_of_s = len(s)
        valid = 0
        res = []
        
        if len_of_words > len_of_s:
            return []
        
        for i in range(len_of_s - len_of_words + 1):
            mapping = dic.copy()
            valid = 0
            for j in range(i, len_of_s - len_of_each_word + 1, len_of_each_word):
                tmp = s[j:j+len_of_each_word]
                if tmp not in mapping:
                    break
                elif tmp in mapping:
                    mapping[tmp] -= 1
                    if mapping[tmp] < 0:
                        break
                    if mapping[tmp] == 0:
                        valid += 1
                    if valid == len(set(words)):
                        res.append(i)
                        break
        return res
        
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordLen = len(words[0])
        wordCount = len(words)
        windowSize = wordLen * wordCount
        freqMap = dict(collections.Counter(words))
        res = []
        
        for i in range(wordLen):
            start = i
            
            #sliding window technique
            while start + windowSize - 1 < len(s):
                substring = s[start : start+windowSize]
                j = wordCount
                temp = {}
                
                while j > 0: 
				    # for each word in the window
                    # get the word, check its freq
                    
                    tempword = substring[wordLen*(j-1) : wordLen*j]
                    count = temp[tempword] + 1  if tempword in temp else 1
                    
                    '''if tempword's freq in temp != tempword's freq in freqMap, 
                    it means tempword does not appear as many times in the 
                    substring as it does in the original string, based on
                    tempword's freq in the words list'''
                    if tempword not in freqMap or count > freqMap[tempword]:
                        break
                    
                    temp[tempword] = count
                    j -= 1
                    
                if j == 0:
                    res += [start]
                start += wordLen * max(j, 1)
        
        return res

