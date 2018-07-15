#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26
# context="""hello word"""
# f=open("hello.txt","w")
# f.write(context)
# # f.close()
# f=open("hello.txt")
# while True:
#     line=f.readline()
#     if line:
#         print(line)
#     else:
#         break
# f.close()
# f=open("hello.txt")
# lines=f.readlines()
# for line in lines:
#     print(line)
# f.close()
# f=open("hello.txt")
# st=f.read(5)
# print(st)
# f.close()
# f=open("hello.txt","w+")
# li=["2","string name ","liuhaitao","裤腰噶 u 太"]
# f.writelines(li)
# # f.write()
# f.close()
# f=open("hello.txt")
# str=f.readline()
# print(str)
# f.closed
import  os
# file("hello.txt","w")
# if os.path.exists("hello.txt"):
#     os.remove("hello.txt")
# # os.mkdir("tese")
# str=os.path.abspath("tese")
# print(str)
# str2=os.path.isdir("tese")
# print(os.path.exists("test"))
# os.renames("tese","test")
# os.open()
# f=open("test/123.txt","w+")
# String="is the file test"
# f.writelines(String)
# f.closed
# print(os.path.isfile("test/123.txt"))
# print(os.renames("test/123.txt","my.txt"))
# f=open("my.txt","w+")
# f.writelines("is just test")
# f.closed
# f=open("my.txt","w+")
# f.writelines("is just test")
# f.closed
# f=open("my.txt")
# str=f.readline()
# s=open("test.txt","w+")
# s.writelines(str)
# f.closed
# s.closed
import shutil
# shutil.copy("test.txt","124.txt")
#os.mkdir("test")
# shutil.move("124.txt","test")
# shutil.copyfile("my.txt","1.txt")
# os.remove("1.txt","test.txt")
# os.renames("1.txt","2.txt")
# f=open("test/test.txt","w+")
# f.writelines("is test")
# f.closed
# os.remove("test")
# files=os.listdir("../")
# for filename in files:
#     pos=filename.find("test.txt")
#     if
# file=os.listdir(".")
# for filename in file:
#     li=os.path.splitext(file)
#     if li[1]==".html" :
#         newname=li[0]+".htm"
#         os.rename(filename,newname)
# os.remove("2.txt")
# f=open("test/test.txt","w+")
# f.writelines("hello word liuhaitao")
# f.closed
import re
# f =open("test/test.txt","r")
# count=0
# for s in f.readlines():
#     li=re.findall("o",s)
#     if len(li)>0:
#         count=count +li.count("o")
# print("查找到"+str(count) +"个 o")
# f.closed
# f=open("test/test.txt","w+")
# f.writelines("hello word liuhaitaodhaia")
# f.closed
#
import os
# def Vist(path):
#     li=os.listdir(path)
#      for p in li:
#          pathname=os.path.join(path,p)
#          if not os.path.isfile(pathname):
#              Vist(path#)
#          else:
#              print(pathname)
#  if __name__=="__main__"
#      path=r""
# import  sys
# sys.stdin=open("test/test.txt","r")
# for line in sys.stdin.readline():
#     print(line)
import sys
# sys.stdout=open(r"test/test.tex","a")
# print("goodle")
# sys.stdout.closed
# def FileInputStr(filename):
#     try:
#         f=open(filename)
#         for line in f:
#             for byte in line:
#                 yield byte
#     except StopIteration as e:
#
#         f.closed
#         return
