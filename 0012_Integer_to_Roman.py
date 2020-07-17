class Solution(object):
    def intToRoman(self, n):
        # TODO convert int to roman string
        string=''
        symbol=['M','D','C','L','X','V','I']
        value = [1000,500,100,50,10,5,1]
        num = 10**(len(str(n))-1)
        # quo = n//num
        # rem=n%num
        quo, rem = divmod(n, num)
        
        if quo in [0,1,2,3]:
            string += symbol[value.index(num)]*quo
            
        elif quo in [5,6,7,8]:
            temp = symbol[value.index(5*num)] + symbol[value.index(num)]*(quo-5)
            string += temp
            
        elif quo in [4,9]:
            temp = symbol[value.index(num)] + symbol[value.index(quo*num+num)]
            string += temp
        
        if rem ==0:
            return string
        else:
            string += self.intToRoman(rem)
        
        return string
    
#         TODO convert int to roman string
#         dic = {1:"I", 5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}

#         s = ""
#         x = 10**(len(str(n)) - 1)

#         div = n/x
#         rem = n%x

#         if div in [0,1,2,3]:
#             s += div * str(dic.get(x))
#         elif div == 4:
#             s += str(dic.get(1*x)) + str(dic.get(5*x))
#         elif div == 9:
#             s += str(dic.get(1*x)) + str(dic.get(10*x))
#         else:
#             s += str(dic.get(5*x)) + (div-5)*str(dic.get(x))
            
#         if rem != 0:
#             s += self.intToRoman(rem)
#         else:
#             return s
#         return s
