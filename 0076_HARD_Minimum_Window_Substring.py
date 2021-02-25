class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        right = 0
        valid = 0 #窗口中满足need条件的字符个数
        res = s + "a" #这个字符之要长度比s多一个字符就可以
        
        needs = collections.defaultdict(int) #每个字符需要出现的次数
        window = collections.defaultdict(int) #窗口中每个字符已经出现的次数
        
        for c in t:
            needs[c] += 1
        
        while right < len(s):
            c = s[right] #移入窗口的字符
            right += 1 #扩大窗口
            # 窗口内数据的更新
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1
                    
            while valid == len(needs.keys()): #左窗口需要收缩的条件
                # 更新最小覆盖子串
                res = s[left:right] if len(s[left:right]) < len(res) else res
                
                d = s[left] #需要移除窗口的元素
                left += 1 #窗口缩小
                # 窗口内数据的更新
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1 
        # 返回最小覆盖子串
        return res if res != s + "a" else ""
    
    
    
    
    
    
    
    
