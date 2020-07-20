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

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        start = 0 
        end = len(letters) - 1
        n =  len(letters)
        while start <= end:
            mid = start + (end - start) / 2
            if target >= letters[mid]:
                start = mid + 1
            else:
                end = mid - 1
            
        return letters[start % n]
