#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26

import os
#
# # for root,dirs,files in os.walk("/usr"):
# #     # for name in dirs:
# #     # #     print(os.path.join(root,name))
# #     #     print(os.path.dirname(name))
# #     # # for name in files:
# #     # #     print(os.path.join(root,name))
# #     # #     print(os.path.basename(name))
# #     #print(root)
# #     #print(dirs)
# #     #print(files)
# #     for name in root:
# #         for name1 in dirs:
# #             for name2 in files:
# #                 print(os.path.join(root,name1,name2))
# #             print(os.path.join(root,name1))
# #         print(os.path.join(root,root))
#
# test=open(r"/Users/apple/Documents/GitHub/my_python/src/Lesson_100/my/124.txt")
# str=test.read()
# print(str)
# test.closed
#
# if os.path.isfile(r"/Users/apple/Documents/GitHub/my_python/src/Lesson_100/my/124.txt"):
#     print("nice")
# else:
#     print("bad")
# class Testmy:
#
#     def __init__(self,name,age):
#
#      self.name=name
#      self.age=age
#
#      def mytest(socre,key):
#
#          if self.score<90:
#              return "good"
#          elif self.score>90:
#              return "good"
#          else:
#              return None
#
#
# list=[1,2,34,5,6,7]
# it=iter(list)
# print(next(it))
# print(next(it))
# for i in it:
#     print (i)
# def fab(max):
#     n,a,b=0,0,1
#     list=[]
#     while n<max:
#         list.append(b)
#         print (b)
#         a,b=b,a+b
#         n+=1
#     return list
# fab(5)
# def fub(max):
#     n,a,b=0,0,1
#     while n < max:
#         yield b
#         a,b=b,a+b
#         n=n+1
# # for n in fub(5):
# #     print(n)
#
# f=fub(10)
# b=f.next()
# print(b)

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b      # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1
for n in fab(7):
    print (n)
f=fab(10)

print(f.next())