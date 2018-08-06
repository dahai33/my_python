#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26
import xml.dom.minidom as xmldom


#使用 minidom 解析器打开 xml 文件
# domobj=xmldom.parse("test.xml")
# print("xmldoem.parse:",type(domobj))
#
# elementobj=domobj.documentElement
# print(type(elementobj))
# sub=elementobj.getElementsByTagName("movie")
# print(type(sub))
# print(len(sub))
#
# print(sub[0].getAttribute("title"))
#
# sub1=elementobj.getElementsByTagName("year")
# print(sub1[0].firstChild.data)

import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement

cc=dom.getElementsByTagName('caption')
c1=cc[0]
print (c1.firstChild.data)

c2=cc[1]
print (c2.firstChild.data)

c3=cc[2]
print (c3.firstChild.data)
