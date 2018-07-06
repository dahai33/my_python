#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 15:18
from __future__ import  division
# x=10
# y=2
# op="+"
# resuout={
#     "+": x+y,
#     "**":x**y,
#     "/":x/y,
#     "-":x-y
# }
# class switch(object):
#     def __init__(self,value):
#         self.value=value
#         self.fall=False
#     def __iter__(self):
#         if __name__ == '__main__':
#             yield match
#             raise StopIteration
#     def match(self,*args):
#         if self.fall or not args:
#             return True
#         elif self.value in args:
#             self.fall=True
#             return True
#         else:
#             return False
##########################
# x=105
# while x>100:
#    x+=1
#    print (x)
# x=5
# j=5
# while (0<x<10):
#     x=x-1
#     while(0<j<10):
#         j=j-1
#         print( "x+j=",x+j,"x=",x ,"y=",j)
##########################
# for  x in range(1,10):
#     for y in range(11,20):
#         print(x,"*",y,"=",x*y)
##########################
#冒泡

def buSort(numbers):
    for j in range(len(numbers)-1,-1,-1):
        for i in range(j):
            if numbers[i]>numbers[i+1]:
                numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
                print (numbers)
def main():
    numbers=[12, 33, 44, 23, 34, 52 ,22]
    buSort(numbers)
if __name__=='__main__':
     main()
##########################
# print (resuout.get(op))
# for case in switch(op):
#     if case ("+"):
#         print(x+y)
#         break
#     if case ("**"):
#         print(x**y)
#         break
#########################
# x=10
# #y=99
# if(x==2):
#     y=10
# elif (x==10):
#     y=20
# else:
#     y=30
# print("y=",y)

