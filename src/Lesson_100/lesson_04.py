#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:2
import datetime as time
# s='liu hai tao da hai! \n '
# print(str(s))
# print(repr(s))
# for x in range(1,11):
#     print(repr(x).rjust(2),'*',repr(x*x).rjust(3),end='=')
#     print(repr(x*x*x).rjust(4))
# for x in range(1,11):
#     print('{0:3d} {1:5d} {2:14d}'.format(x,x*x,x*x*x))
#table={'abc':1,'bcd':2,'def':3}
#print('abc:{abc:d}; bcd:{bcd:d};def:{def:d}'.format(table))

import time
localtime=time.localtime(time.time())
loca=time.asctime(time.localtime(time.time()))
print(loca)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strftime(a,"%a %b %d %H:%M:%S %Y")))