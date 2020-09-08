class Solution(object):
    # 自己解法比较慢
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def foo(num):
            if num == 0:
                return [1]
            # if num == 1:
            #     return [1,1]
            prev = foo(num-1)
            return [1] + [prev[i] + prev[i+1] for i in range(num-1)] + [1] 
        res = []
        for i in range(numRows):
            res.append(foo(i))
        return res
    # 官方解法快一倍
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            # 定义一个指定长度的数组 值全部为none
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1
            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)
        return triangle
