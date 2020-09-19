class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # time:O(N^2)，space:O(1)。
        # 首先，数组长度小于2的时候，必然是0。
        # 其次，观察到a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1],
        # b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k],
        # 那么根据位运算的规则， a^b=arr[i]^ arr[i + 1] ^ ... ^ arr[k]，即i到k。
        # 此外，根据位运算，如果a^b==0,那么a==b，这是逆否命题，即反推也成立。
        # 而固定了两端之后，中间的j可以任意取，故有k-i种。每次计算完，如果满足条件，在ans里加上k-i即可。

        if len(arr) < 2:
            return 0
        res = 0
        for i in range(len(arr)):
            temp = arr[i]
            for j in range(i+1, len(arr)):
                temp ^= arr[j]
                if temp == 0:
                    res += j - i
        return res
