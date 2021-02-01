class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        for i, v in dic.items():
            if v == 1:
                return i
            
    # 异或 相同的数异或结果为0， 任何数和0的异或就是它本身      
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)
