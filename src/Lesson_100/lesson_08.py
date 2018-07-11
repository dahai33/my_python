# #!/usr/bin/python3
# #Author:刘海涛
# # --*-- coding: uft-8 --*--
# # @Time   : 19:32
# #@字符串正则表达
# #字符串格式
# str="version3.0"
# # num=1.0
# # # sum =100
# # # format="%s" % str1
# # # #format="%s,%.4f,%%" %(str1,num,sum)
# # # format="%,%" % sum
# # # print(format)
# # print(str.center(20))
# # print(str.center(20,"*"))
# # print(str.rjust(30))
# # print(str.ljust(5))
# # print("%50s" % str)
# #字符串的转换
# path="liu\hai\tao\da\hai"
# # print(path)
# # print(len(path))
# # path=r"hellow\word\a"
# # print(path)
# # print(len(path))
# #去掉字符串中的转移符 strip() lstrip() rstip()
# # print(path)
# # print(path.strip())
# # print(path.lstrip())
# # print(path.rstrip())
# # 字符串的合并
# # str="liuhaitao"
# # str1="nice"
# # str2="good"
# # print(str + "%5s" % str1 + "%5s" % str2)
# # Strs=["hello","word","china"]
# # result="".join(Strs)
# # print(result)
# # from functools import reduce
# # import operator
# # re=reduce(operator.add,result,"")
# # print(re)
# # print(str[3:9])
# # st="bad nic: 1,2 3,5"
# # print(st.split())
# # print(st.split(","))
# # print(st.split(",",2))
# # s="a"
# # print(id(s))
# # print(id(s+"b"))
# ##字符串的比较 ==   ！=
# # str="abc"
# # str1="abc"
# # str2="ABC"
# # if(str != str2):
# #     print("nice")
# # else:
# #     print("bad")
# #字符串的翻转
# # def reverse(s):
# #     out=""
# #     li=list(s)
# #     for i in range(len(li),0,-1):
# #         out +="".join(li[i-1])
# #     return out
# # print(reverse("abcdsef"))
# #字符串的替换
# # str="this is a apple."
# # #头部开始查找
# # print(str.find("a"))
# # #尾部开始查找
# # print(str.rfind("a"))
# # #字符串的替换
# # str1="hello liu hai hello liu"
# # print(str1.replace("hello","nice",4))
# # print(str1.replace("liu","tao"))
# ##字符串和日期的转换
# # import time, datetime
# # print(time.strftime("%Y-%m-%d %X",time.localtime()))
# # print(time.localtime())
# #字符串的正则表达尺
# import re
