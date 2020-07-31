class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            if a < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] == abs(a):
                        stack.pop()
                        break
                    elif stack[-1] < abs(a):
                        stack.pop()
                    else:
                        break
                else:
                    stack.append(a)
        return stack
