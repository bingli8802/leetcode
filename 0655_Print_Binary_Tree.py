# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        # 1.计算高度
        def countHeight(root):
            if not root:
                return 0
            return max(countHeight(root.left), countHeight(root.right)) + 1
        height = countHeight(root)
        columns = 2**height - 1 # 列数/列的最大长度
        rows = height # 行数
        # 2.构建二维数组
        array = [[""]*columns for _ in range(rows)]
        # 3.dfs 二分填充数组（从中间即root位置分割开，分别往左、往右递归填充）
        def dfsPaint(node, array, row, start, end):
            if not node or start > end:
                return
            if start == end:
                array[row][start] = str(node.val)
            else:
                # 渲染当前结点，在树的中间位置
                middle = start + (end - start) // 2
                array[row][middle] = str(node.val)
                # 左子树渲染
                dfsPaint( node.left, array, row + 1, start, middle - 1)
                # 右子树渲染
                dfsPaint(node.right, array, row + 1, middle + 1, end)
        dfsPaint(root, array, 0, 0, columns-1)
        return array
        
