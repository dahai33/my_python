#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 20:26
import  sys
#List的访问方法
my_list=['ea','bd','ce','ed','ee','ff']
my_list_1=[2,2,3,40,5,6,70,8,9,10]
# print(len(my_list))
# print(str(my_list))
# ####列表中的添加、插入、删除
# my_list.append("test")
# print(str(my_list))
# my_list.insert(0,"just")
# print(str(my_list))
# my_list.remove("a")
# print(str(my_list))
# print(my_list.pop())
# ##列表中的元素可以修改移动删除
# print(my_list[1:3])
# for i in  range(len(my_list)):
#     print(my_list[i] )
list=my_list+my_list_1
# print(str(list))
###列表的查找 翻转、排序
# my_list_1.sort()
# print(my_list_1)
# my_list_1.reverse()
# print(my_list_1)
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)
####list常用的方法
#在列表末端添加append
# 在列表末端添加appendmy_list_1.append(99)
# print(my_list_1)
# my_list_1.insert(13,999)
# print(my_list_1)
# my_list_1.remove(9)
# print(my_list_1)
# my_list_1.pop()
# print(my_list_1)
# #index(value,[start,[stop]])
# # my_list_1.index(5,[2,[-1]])
#
# print(my_list_1)
# #堆栈后进先出
# my_list_1.append(123)
# print(my_list_1)
# my_list_1.pop()
# print(my_list_1)
# #先进先出
# my_list_1.insert(0,123)
# my_list_1.pop()
# print(my_list_1)
#####创建迭代器对象
#it =iter(list)
#for x in it:
#    print ("x=",x)
###next 方法
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit();
#list.conunt(x) 返回 x在 list 中的次数
# s=list.count(2)
# print (s)
# print(list.count(2))
print(sys.path)
print (sys.version)



