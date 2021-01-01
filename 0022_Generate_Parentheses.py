class Solution(object):
    # 回溯算法 套用模版
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backTrack(left, right, path):
            # 当左右括号都用完 生成一个合法path
            if left == 0 and right == 0:
                res.append(path)
                return
            # 可以添加左括号
            if left > 0:
                backTrack(left - 1, right, path + '(')
            # 当前左括号如果大于右括号数量 可以添加一个右括号
            if left < right:
                backTrack(left, right - 1, path + ')')
        backTrack(n, n, '')
        return res
