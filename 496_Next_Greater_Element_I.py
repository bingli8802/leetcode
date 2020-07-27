class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # 遍历nums2
        # 如果stack==empty 就把nums2第i个元素放入stack
        # 如果stack!=empty 就比较i和stack最后一个元素
            # 如果i大于stack最后一个元素 就把i和stack最后一个元素配对 放入dict 再把i放入stack
            # 如果i不大于stack最后一个元素 就把i放入stack
        hash_dict = dict()
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                hash_dict[stack.pop()] = i
            stack.append(i)
        return [hash_dict.get(i,-1) for i in nums1]
            
