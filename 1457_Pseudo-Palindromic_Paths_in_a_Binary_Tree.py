# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# dict储存节点和节点个数
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def travel(node, counter):
            counter[node.val] += 1
            # 如果是叶节点的话，判断是否是伪回文
            if node.left == None and node.right == None:
                # 取出所有计数伪奇数的数值
                odds = [k for k,v in counter.items() if v%2==1]
                if len(odds) < 2:
                    self.ans += 1
            else:
                # 如果有左节点 递归 并更新counter的值
                if node.left: 
                    travel(node.left, counter)
                    # 这个步骤很关键
                    counter[node.left.val] -= 1
                # 如果有右节点 递归 并更新counter的值
                if node.right: 
                    travel(node.right, counter)
                    # 这个步骤很关键
                    counter[node.right.val] -= 1
        # 用到collections.defaultdict(int)这个方法
        travel(root, collections.defaultdict(int))
        return self.ans
# dict储存节点和节点个数
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def travel(node, counter):
            if node.val in counter:
                counter[node.val] += 1
            else:
                counter[node.val] = 1
            # 如果是叶节点的话，判断是否是伪回文
            if node.left == None and node.right == None:
                # 取出所有计数伪奇数的数值
                odds = [k for k,v in counter.items() if v%2==1]
                if len(odds) < 2:
                    self.ans += 1
            else:
                # 如果有左节点 递归 并更新counter的值
                if node.left: 
                    travel(node.left, counter)
                    # 这个步骤很关键
                    counter[node.left.val] -= 1
                # 如果有右节点 递归 并更新counter的值
                if node.right: 
                    travel(node.right, counter)
                    # 这个步骤很关键
                    counter[node.right.val] -= 1
        # 用到collections.defaultdict(int)这个方法
        travel(root, {})
        return self.ans
# 二进制
# 利用二进制前缀和快速验证是否是回文串。
# 验证思路：因为数据范围是0-9，位数很固定。故用一个最长10位的2进制数字保存累计状态。
# 每次遍历到新节点数据时，对相应位数数字进行异或操作。如果该位数是1，说明累计奇数个，是0说明累计偶数个。
# 遍历到叶子节点后，看累计状态是否最多只有一个1,如果是就说明该路径是回文路径。
class Solution:
    def pseudoPalindromicPaths (self, root):
        self.ans = 0
        def travel(node, mask):
            mask = mask ^ (1 << node.val)
            print mask
            if not (node.left or node.right):
                if (mask & (mask-1) == 0 or mask == 0):
                    self.ans += 1
            else:
                if node.left: travel(node.left, mask)
                if node.right: travel(node.right, mask)
        travel(root, 0)
        return self.ans

