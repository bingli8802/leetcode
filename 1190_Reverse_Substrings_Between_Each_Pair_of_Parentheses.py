class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ['']
        for i in s:
            # 左括号的话就添加一个空字符串
            if i == "(":
                ans += ['']
            # 右括号的话就把栈顶元素反转 并存储到前一个字符上 最后删除栈顶元素
            elif i == ")":
                ans[-2] += ans[-1][::-1]
                ans.pop()
            # 把字符全部存储在ans最顶字符串里
            else:
                ans[-1] += i
        return ans[0]
