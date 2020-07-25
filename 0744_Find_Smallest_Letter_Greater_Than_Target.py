# class Solution(object):
#     def nextGreatestLetter(self, letters, target):
#         """
#         :type letters: List[str]
#         :type target: str
#         :rtype: str
#         """
#         left = 0
#         right = len(letters)-1
        
#         while left < right:
#             middle = (left+right)/2
#             if letters[middle] > target:
#                 right = middle
#             else:
#                 left = middle + 1
#         return letters[left] if letters[left] > target else letters[0]

# class Solution(object):
#     def nextGreatestLetter(self, letters, target):
#         left = 0 
#         right = len(letters) - 1
#         n =  len(letters)
#         while left <= right:
#             mid = left + (left - right) / 2
#             if target >= letters[mid]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
            
#         return letters[left % n]

# 第一遍复习写出
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)
        while left < right:
            mid = (left+right)/2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[right%len(letters)]
