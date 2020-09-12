class Solution(object):
    # 利用二进制数的数学性质
    #遍历A，每增加一个元素，那么二进制数为前面所有元素组成的二进制数乘以2，加上当前元素
    #因为只考虑是否能被5整除，那么每次运算只取模5的结果即可，随着遍历迭代temp，将模5的结果加入ans即可
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ans = []
        tmp = 0
        for i in A:
            tmp = (tmp * 2 + i) % 5
            # tmp = tmp * 2 + i
            ans.append(tmp % 5 == 0)
        return ans
