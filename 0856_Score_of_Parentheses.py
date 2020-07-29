class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        score = [0]
        for i in S:
            if i == "(":
                score.append(0)
            else:
                depth = score.pop()
                score[-1] += max(2*depth, 1)
        return score.pop()
