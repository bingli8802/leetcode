class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        i = 0
        while i < len(S):
            j = i + 1
            while j < len(S):
                if S[i] != S[j]:  
                    break
                else:
                    j += 1
            if j - i >= 3:
                ans.append([i, j-1])
            i = j
        return ans
    
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        i = 0
        while i < len(S):
            j = i + 1
            while j < len(S):
                if S[i] != S[j]:  
                    break
                else:
                    j += 1
            ans.append([i, j-1])
            i = j
        return [pair for pair in ans if (pair[1] - pair[0] + 1) >= 3]

