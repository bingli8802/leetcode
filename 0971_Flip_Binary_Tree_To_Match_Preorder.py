class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.ans = []
        self.flag = True
        def dfs(r):
            # 如果根节点存在 并且flag为true
            if r and self.flag:
                #如果voyage为空 或 当前树值无法匹配数列首元素，flag=false
                if not voyage or r.val != voyage.pop(0):    
                    self.flag = False
                #如果两子树都存在且右子树等于数列的首元素，就需要交换左右子树
                elif r.left and r.right and r.right.val == voyage[0]:   
                    self.ans += [r.val]
                    dfs(r.right)
                    dfs(r.left)
                # 如果两个子树都存在且左子树等于数列首元素，不需要交换左右子树，继续向下递归
                else:                                       
                    dfs(r.left)
                    dfs(r.right)
        dfs(root)
        return self.ans if self.flag else [-1]
