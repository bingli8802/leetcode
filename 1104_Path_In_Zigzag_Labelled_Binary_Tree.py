class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        # 思路就是看在正常编号的二叉树中，“之” 字形是怎样的路径
        # 在正常二叉树上按“之” 字形寻路就是每次跳到该层对称的子树上
        # int(math.log(label,2))用来计算层数
        ans = []
        while label:
            ans.insert(0, label)
            # label = 3 * 2 ** (len(bin(label))-3) - 1 - label
            label = 3 * 2 ** (int(math.log(label,2))) - 1 - label
            label =  label / 2
        return ans
