class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # 每次找最大值 然后翻转最大值之前数字 再翻转整个数组 O(n^2)
        res = []
        for i in range(len(arr), 1, -1):
            # 找到最大值的index
            idx = arr.index(i)
            # 把最大值后面的数字翻转 再加上最大值前面的数字
            arr = arr[:idx:-1] + arr[:idx]
            # 结果就是最大值的位置进行一次反转 再一次反转
            res += [idx + 1, i]   
        return res

