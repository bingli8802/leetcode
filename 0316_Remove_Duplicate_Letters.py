class Solution(object):
    # 参考网上答案 单调栈  
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cnt = collections.Counter(s)
        for char in s:
            if char not in stack:
                while stack and stack[-1] > char and cnt[stack[-1]] > 0:
                    stack.pop()
                stack.append(char)
            cnt[char] -= 1
        return "".join(stack)
    
    # 解法一样 多加一个set存储数据
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        seen = set()
        remain_counter = collections.Counter(s)

        for char in s:
            if char not in seen:
                while stack and char < stack[-1] and remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
            remain_counter[char] -= 1
            # print seen, stack
        return ''.join(stack)


