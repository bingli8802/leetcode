class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x
        
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        li = sorted(map(str, nums), key = LargerNumKey)
        largest_num = ''.join(li)
        # [0,0] ---> '00' 这种情况返回‘0’就可以了
        return '0' if largest_num[0] == '0' else largest_num

        
