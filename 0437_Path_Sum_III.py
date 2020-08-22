# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 每次递归中，传入的sumlist是不是都指向同一个栈?那么在return语句中的两个递归函数中所传入的sumlisit是不相同的数组,所以是不是应该在传入前，将sumlist复制，将复制数组用来传参数?
# 首先系统会有一个栈，用来保存每一轮递归的所有参数，当后面return返回的时候，在相同的递归层，所有的参数都是相同的。 也就是说，在同一深度的递归层次下，return语句中的sumlist是相同的，即使可能这两个递归语句后面的深度不一样，但是返回到这一层的时候，还是用到的之前系统存储的这一层递归的参数.
# 必须要将这个数组复制一份,使得进入下次递归是另一个数组,而不是在原有数组上面修改。如果是在原有数组上修改，那么每层递归都会对这个数组进行操作，所以return之后再次回到这一层的时候，不是我们之前需要的那个数组了。但是这时候二叉树的其它树枝可能还是会用到之前的那个数组.
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root, sumlist):
            if not root:
                return 0
            # 数组的复制 不要用append 那样会直接修改原来数组
            sumlist = [num + root.val for num in sumlist] + [root.val]
            count = sumlist.count(sum)
            return count + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root, [])
