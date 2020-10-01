class Solution(object):
    # 和自己思路是一样的 但这个方法更好 
    # tmp永远是前一个元素的值 如果不是tmp的子目录就更新tmp 
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        res = []
        tmp = ' '
        folder.sort()
        for f in folder:
            if not f.startswith(tmp):
                res.append(f)
                tmp = f + '/'
        return res
