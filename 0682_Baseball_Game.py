class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        li = []
        res = 0
        for op in ops:
            sum = 0
            if op == "D" and li:
                li.append(li[-1]*2)
            elif op == "C" and li:
                li.pop()
            elif op == "+":
                # if len(li) == 1:
                #     sum = li[-1]
                # elif len(li) >= 2:
                #     sum = li[-1] + li[-2]
                # li.append(sum)
                
                # 或者直接一句话
                # li.append(li[-1] + li[-2])
                
                # 或者完全用栈的操作
                top = li.pop()
                new_top = top + li[-1]
                li.append(top)
                li.append(new_top)
            else:
                li.append(int(op))
        for i in li:
            res += i
        return res
                
