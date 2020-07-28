class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 用来存放 index 和 "(" ")"
        res = []
        li = list(s)
        # 用enumerate迭代,会形成[key,value],把他们放入res
        for key, val in enumerate(s):
            # 遇到"("就放进栈
            if val == "(":
                res.append([key, val])
            # 遇到")"再进行判断
            elif val == ")":
                # 如果栈不空,并且栈顶元素是"(",就把栈顶元素pop出来
                if len(res) != 0 and res[-1][1] == "(":
                    res.pop()
                # 如果栈空，就把")"push到栈
                else:
                    res.append([key,val])
        # 把栈里的元素从s里pop出去 注意元素index随着s的减少也变小
        for key, val in enumerate(res):
            pop_index = val[0] - key
            li.pop(pop_index)
        return "".join(li)
