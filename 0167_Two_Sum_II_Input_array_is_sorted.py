class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
#       用两个指针，一个头一个尾
#       如果小于target，左边右移，如果大于target，右边左移
        i, j = 0, len(numbers)-1
        ret = []
        
        while i < j:
            if numbers[i] + numbers[j] == target:
                ret = [i+1,j+1]
                return ret
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else: 
                i += 1
        return ret
