# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): 
#   v.append(i.next())

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list()
        
        # 逆序存入，stack弹出才是正序
        for ni in reversed(nestedList):
            self.stack.append(ni)
        # print (self.stack)
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        """
        flattern until find a integer
        """
        while self.stack:
            # 如果栈顶就是integer，那么可以停止寻找，直接返回True
            if self.stack[-1].isInteger(): 
                return True
            # 不然的话就是list，存进栈里继续找，注意逆序存入，才能顺序取出
            for ni in reversed(self.stack.pop().getList()):
                self.stack.append(ni)
        
        return False
    
