class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        0 1 2 3 4 5 6 7 8 9 10 11 12 13
        ) ) ) ( ( ) ( ) ( ( (   ) (   ) 
        [ ]
        [ ]
        '''
        len_s = len(s)
        index_stack = []
        p_stack = []
        max_len = 0
        for i in range(len_s):
            if s[i] == '(':  
                p_stack.append(s[i])      
            elif s[i] == ')':
                if not p_stack:
                    index_stack.append(i)
                elif p_stack and p_stack[-1] == ')':
                    index_stack.append(i)
                elif p_stack and p_stack[-1] == '(':
                    p_stack.pop()
        
        if not index_stack:
            return len_s
        
        for idx in range(len(index_stack)):
            if idx == 0:
                max_len = max(max_len, index_stack[0])
            else:
                max_len = max(max_len, index_stack[idx] - index_stack[idx-1] - 1)
                
        max_len = max(max_len, len(s) - index_stack[-1] - 1)
        return max_len           
                    
    def longestValidParentheses(self, s):
        ans=0       # 最大合法长度(返回值)
        stack=[-1,]  # stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
        for i,ch in enumerate(s):
            if '('==ch:  # 左括号
                stack.append(i)
            elif len(stack)>1:  # 右括号，且有成对左括号
                stack.pop()     # 成对匹配
                ans = max(ans, i - stack[-1])
            else:   # 非法的右括号
                stack[0]=i
        return ans

                    
                    
            
            
        
