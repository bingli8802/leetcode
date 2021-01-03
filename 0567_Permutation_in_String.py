class Solution(object):
    # 使用普通字典dict
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        left, right, valid = 0, 0, 0
        needs = {}
        window = {}
        
        for c in s1:
            if c in needs:
                needs[c] += 1
            else:
                needs[c] = 1
                
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in needs:
                if c in window:
                    window[c] += 1
                else: 
                    window[c] = 1  
                if window[c] == needs[c]:
                    valid += 1
            # print "window: [%d, %d]" % (left, right)      
            while (right - left) >= len(s1):
                if valid == len(needs):
                    return True
                else:
                    d = s2[left]
                    left += 1
                    if d in window:
                        if window[d] == needs[d]:
                            valid -= 1
                        window[d] -= 1
        return False
    
    # 使用defaultdict字典
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        left, right, valid = 0, 0, 0

        needs = collections.defaultdict(int)
        window = collections.defaultdict(int)
        
        # need里每个字符需要的个数
        for c in s1:
            needs[c] += 1
                
        while right < len(s2):
            c = s2[right] #要移动到窗口的字符
            right += 1 #扩大窗口
            # 窗口内字符的更新
            if c in needs:  
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1
            # print "window: [%d, %d]" % (left, right)      
            
            while (right - left) >= len(s1): # 收缩左边界
                if valid == len(needs):
                    return True
                d = s2[left] #将要移除窗口的字符
                left += 1 #收缩窗口
                # 窗口内字符的更新
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        return False
