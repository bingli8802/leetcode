class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1   
        idx = 0
        
        while idx < len(chars)-1 :
        
            left = chars[idx][0]
            right = chars[idx+1][0]
            
            if left == right:
                count += 1
                right = right + str(count)
                idx = chars.index(left)
                chars.remove(left)
                
            elif left != right:
                count = 1
                idx += 1
                
 class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1   
        idx = 0
        
        while idx < len(chars)-1 :
            
            if chars[idx] == chars[idx+1]:
                count += 1
                chars.pop(idx+1)
                
            elif chars[idx] != chars[idx+1]:
                if count == 1:
                    idx += 1
                else:
                    for i in list(str(count)):
                        chars.insert(idx+1, i)
                        idx +=1
                    count = 1
                    idx +=1
        if count != 1:
            chars.extend([i for i in list(str(count))])
            return len(chars)
        
        return len(chars)
                
  class Solution(object):
    def compress(self, chars: List[str]) -> int:
        cnt, i  = 1, 0    #指针初始化
        while i < len(chars)-1:
            if chars[i]==chars[i+1]:
                cnt += 1    #重复就计数加1
                chars.pop(i+1)    #并且把重复的元素pop掉
            elif  chars[i]!= chars[i+1]:
                if cnt==1:
                   i+=1    #如果是单元素，就忽略，指针后移1位
                else:     #否则就把计数cnt， 字符列表化，逐位插入到后面
                    for cnt in list(str(cnt)):
                        chars.insert(i+1,str(cnt))
                        i +=1     #每插入一个数字，指针后移一位
                    cnt = 1
                    i = i+1    #初始化计数，cnt=1, 插入所有的cnt后，指针后移一位
        if cnt != 1:    #处理最后一组计数，如果不是1，逐位插入cnt字符
            chars.extend([str(x) for x in list(str(cnt))])
            return len(chars)
        else: return len(chars)    #最后一组cnt=1，省略计数字符

