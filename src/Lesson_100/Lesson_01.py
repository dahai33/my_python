#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:24
# 局部变量#
local=1
def fun():
    local=1
    print("局部变量local")
fun()
#global 用于全局变量的引用 类型定义使用
int=10
str="hello word"
#输出字符串
str1="hello:\"liuhaitao\"!"
str2='''liu"haitao"'''
#换行
str3="liuhaitaodhaia@sina.com \n password"
#输出特殊字符
str4="##### ***** () $$ %%%"
i=2**38
print(i)
print("###$$$")
print(str1)
print(str2)
print(str3)
print(str4)
##第一章课后题
# def sum(i ,sum ):
#     if(i<0)：
#         print("请输入大于0的参数")
#     elif(i==0)：
#         print("您输入的参数为0")
#     else：
#         for a < i:
#             sum=sum+i
#             print(sum)
#数据类型
#Number
a,b,c  =10,20,30
#String
b="this is String"
#List
my_list=["a","b","c","d"]
print(my_list[3:4])
#Tuple 元组
my_tuple=("1994","1995","liuhaitao","liuhaitaodahai")
print(my_tuple[1:3])
#Sets集合
Student={"apple","tomcat","tom","jieken "}
if "apple" in Student:
    print("is in")
else:
    print("not in")

#Dictionaires 字典
dic={'name':'tome','age':'12','shcool':'beijin'}
print(dic['name'])



