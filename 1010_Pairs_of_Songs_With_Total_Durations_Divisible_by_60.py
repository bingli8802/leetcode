class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # 不用defaultdict解法1
        # Hashtable = {}
        # for i in time:
        #     Hashtable[i%60] = Hashtable.get(i%60, 0) + 1
        
        # 不用defaultdict解法2
        # dic={}
        # for i,t in enumerate(time):
        #     r = t % 60
        #     dic.setdefault(r,0)
        #     dic[r]+=1
        res = 0
        dic = collections.defaultdict(int)
        for i in time:
            dic[i%60] += 1
        # 使用range(0,31) 巧妙的避免了重复计算
        for k in range(0,31):
            sub = 60 - k
            if k == 0 or k == 30:
                res += dic[k] * (dic[k] - 1) / 2
            elif k not in [0, 30] and sub in dic.keys():
                res += dic[k] * dic[sub]
        return res
