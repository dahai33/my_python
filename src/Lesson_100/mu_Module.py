#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:32

# def func():
#     print("is nice")
# class Myclass:
#     def myfunc(self):
#         print("Mymodule.class.myfunc")
def func(x):
    if x>0:
        return x
    print(filter(func(),range(-9,10)))
    print(list(filter(func(),range(-9,10))))
    func(100)