# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 前序遍历 根节点永远在index[0]
        def preorder(root):
            if not root:
                return ['#']
            return [root.val] + preorder(root.left) + preorder(root.right)
        # 把list转换成字符串
        print preorder(root)
        return ' '.join([str(i) for i in preorder(root)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 把字符串转换成list
        data = iter(data.split(" "))
        def buildTree():
            v = next(data)
            if v == "#":
                return None
            node = TreeNode(int(v))
            node.left = buildTree()
            node.right = buildTree()
            return node
        return buildTree()
    
        # data = data.split(" ")
        # def buildTree():
        #     val=data[0]
        #     del data[0]
        #     if val == "#":
        #         return None
        #     node = TreeNode(int(val))
        #     node.left = buildTree()
        #     node.right = buildTree()
        #     return node
        # return buildTree()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
