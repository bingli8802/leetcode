class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left = 0
        right = len(citations)-1
        while left <= right:
            mid = (left+right)/2
            # 判断中间值很巧妙
            if citations[mid] == len(citations)-mid:
                return citations[mid]
            elif citations[mid] > len(citations)-mid:
                right = mid - 1
            else:
                left = mid + 1
        # 返回值也很巧妙运用减法，这样如果citations==[]也可以返回0
        return len(citations) - left

