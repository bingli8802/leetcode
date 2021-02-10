class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        def mergeSort(arr): 
            tmp = []
            n = len(arr)
            if n == 1:
                return arr
            mid = n / 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            l = 0
            r = 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    tmp.append(left[l])
                    l += 1
                else:
                    tmp.append(right[r])
                    r += 1
                    self.cnt += len(left) - l
            tmp += left[l:]
            tmp += right[r:]
            return tmp

        self.cnt = 0
        mergeSort(nums)
        return self.cnt

    def __init__(self):
        self.count = 0
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.merge_sort(nums)
        return self.count
    
    def merge_sort(self,alist):
        if len(alist)<=1:
	        return alist #如果最后划分只有一个，直接返回
        mid = len(alist)//2  #对半划分
        left = self.merge_sort(alist[:mid]) #继续划分左半边
        right = self.merge_sort(alist[mid:]) #继续划分右半边
        return self.merge(left,right)  #将左右半边返回的进行合并
    
    def merge(self,left,right):
        i = 0
        j=0
        result = []
        while i < len(left) and j < len(right):
	        if left[i]<=right[j]:
		        result.append(left[i])
		        i+=1
	        else:
		        result.append(right[j])
		        j+=1
		        self.count+=(len(left)-i) #增加的地方
        result +=left[i:]
        result+=right[j:]
        return result
