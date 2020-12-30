# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # 前序遍历
    # 把一棵二叉树序列化成字符串
    def serialize_core(self, root, sequence):
        if root is None:
            sequence.append('#')
            return
        sequence.append(str(root.val))
        self.serialize_core(root.left, sequence)
        self.serialize_core(root.right, sequence)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        sequence = []
        if root is None:
            return ''
        self.serialize_core(root, sequence)
        # print sequence
        return ','.join(sequence)
    
    # 把字符串反序列化成二叉树
    def deserialize_core(self, sequence):
        first = sequence.pop(0)
        if first == '#':
            return None
        root = TreeNode(first)
        root.left = self.deserialize_core(sequence)
        root.right = self.deserialize_core(sequence)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root = None
        if data == '':
            return root
        sequence = data.split(',')
        # print(sequence)
        return self.deserialize_core(sequence)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
