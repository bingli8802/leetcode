class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = []
        for i in range(ord('a'), ord('z') + 1):
            dic.append(chr(i))
        # alpha = 'abcdefghijklmnopqrstuvwxyz'
        # dic = list(alpha)
        li = list(s)
        
        if li[0] == "?" and len(li) == 1:
            li[0] = random.choice(dic)
        for i in range(len(li)):
            if li[i] == '?':
                if i == 0:
                    li[i] = random.choice([x for x in dic if x != li[i+1]])
                elif i == len(li)-1:
                    li[i] = random.choice([x for x in dic if x != li[i-1]])
                else:
                    li[i] = random.choice([x for x in dic if x != li[i-1] and x != li[i+1]])
        return li
