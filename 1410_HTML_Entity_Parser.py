class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        dic = {"&quot;": '\"', "&apos;": "'", "&amp;": "&", 
               "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        return text.replace('&quot;','"').replace('&apos;',"'").replace('&gt;','>').replace('&lt;','<').replace('&frasl;','/').replace('&amp;','&')

# class Solution(object):
#     def entityParser(self, text):
#         """
#         :type text: str
#         :rtype: str
#         """
#         dic = {"&quot;": '\"', "&apos;": "'", "&amp;": "&", 
#                "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
#         i = 0
#         while i < len(text):
#             s = ""
#             # 往后查找 直到出现&
#             if text[i] == "&":
#                 # 把&放入s
#                 s += text[i]
#                 # j指向i下一个元素
#                 j = i + 1
#                 # 寻找";" 如果找到了就停止查找
#                 while j < len(text): 
#                     if text[j] != ";":
#                         s += text[j]
#                         j += 1
#                     else:
#                         s += text[j]
#                         j += 1
#                         break
#                 # 判断s是否出现在dic里面 并替换s
#                 if s in dic.keys():
#                     text = text[:i] + dic[s] + text[j:]
#                     i += 1
#                 # 如果s不在dic里面 i就等于j的位置
#                 else:
#                     i = j
#             else:
#                 i += 1
#         return text
