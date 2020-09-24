class Solution(object):
    # 编号和已开灯数目比较，相等则满足 效率高
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        now_sum = cnt = max_num = 0
        for i, v in enumerate(light):
            now_sum += 1
            max_num = max(v, max_num)
            if max_num == now_sum:
                cnt += 1
        return cnt
    
    # 效率很高
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        #判断当前情况下，当前light[i]与1之间是否连续，如果连续则蓝灯
        answer = 0
        max_num = 0
        for index_i,i in enumerate(light):
            if max_num < i:
                max_num = i
            if index_i+1 == max_num:
                answer += 1
        return(answer)
