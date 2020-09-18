class Solution(object):
    # 效率略低
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        # a = [2,13,3,11,5,17,7]
        # b = [2,3,5,7,11,13,17]
        # 想要从a得到b：
        # 1.从a头部拿一个数出来，从尾部添加到b中；
        # 2.从a头部拿一个数，添加到a的末尾。
        
        # 先在逆转过来操作：
        # 2.从b尾部拿一个数，添加到a头部；
        # 1.从a尾部拿一个数，添加到a头部。
        
        deck.sort()
        i=0
        res = collections.deque()
        while deck:
            if i % 2 == 0:
                res.appendleft(deck.pop())
            else:
                res.appendleft(res.pop())
            i += 1
        return res
    
    # 运行最快 综合解法1和解法3
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        res = collections.deque()
        res.append(deck.pop())
        for i in reversed(deck):
            res.appendleft(res.pop())
            res.appendleft(i)
        return res
    
    # 效率高    
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck = sorted(deck)
        ans = [deck.pop()]
        for val in reversed(deck):
            ans.append(ans.pop(0))
            ans.append(val)
        return ans[::-1]

