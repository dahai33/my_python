#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 15:44
import argparse

# parse=argparse.ArgumentParser()#创建实例对象
# #parse.parse_args()# 解析
# parse.add_argument("ehco")# 添加参数
# args=parse.parse_args()
# print (args.echo)

import os
import yaml
# f=str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "Lesson_100/yaml/yaml_01.yaml")))
# print(str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "Lesson_100/yaml/yaml_01.yaml"))))
# # print(os.path.basename(str))
# f=open(r"D:/Object/my_python1/src/Lesson_100/yaml/yaml_test.yaml")
# # content=yaml.load(f)
# # print(type(content))
# # print("修改前",content)
# # content['age']=99
# # content['chidren'][1]['age']=88
# # print("修改后",content)
# # print(content['name'])
# # print(content.keys())
# # print(content.values())
# # print(content.get("chidren")[1].get("name"))

##ospath
import time
# print(os.path.abspath("yaml_test.yaml"))
#os.path.basename(r "D:\Object\my_python1\src\Lesson_100\Lesson_10.py")
# print(os.path.abspath("yaml_test.yaml").split("\\"))
# print(os.path.abspath("yaml_test.yaml").splitlines())
# print(os.path.abspath("yaml_test.yaml").isspace())
# print(os.path.basename("yaml_test.yaml"))
# print(os.path.dirname("yaml_test.yaml"))
# print(os.path.getatime("D:/Object/my_python1/src/Lesson_100/yaml/yaml_test.yaml"))
# print(os.path.getsize("D:/Object/my_python1/src/Lesson_100/yaml/yaml_test.yaml"))
# print(os.path.dirname("D:/Object/my_python1/src/Lesson_100/yaml/yaml_test.yaml"))
#print(os.path.basename("yaml_test.yaml"))
# print(os.path.join("../","Lesson_100/yaml/yaml_test.yaml"))
# print(os.path.abspath("").join(os.path.basename("/yaml_test.yaml")))
# f=open(os.path.join(os.path.abspath(""),"Lesson_100\yaml\yaml_test.yaml"))
# f=open(os.path.abspath())
# co=yaml.load(f)
# print(co)
# str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data/config.ini")))
# print(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir,"yaml/yaml_test.yaml")))
# print(os.path.abspath(os.path.join()))
# print(os.path.dirname(__file__))
# # print(os.pardir)
# # print(os.path.pardir)
# print(os.path.dirname(__file__),os.pardir,"yaml/yaml_test.yaml")
# print(os.path.dirname(__file__),"/yaml/yaml_test.yaml")
# print(os.path.dirname(__file__).join("/yaml/yaml_test.yaml"))

def func(a,b,c):
    return a,b,c
list=[1,2,3]
def func_1(*list):
    return list
#args 元组
def func_2(*args):
    return args
def func_3(a,*args):
    print("this is a=",a)
    print("args in tuple")
    for i in args:
        print(i)
def sums(*args):
    return sums()



if __name__ == '__main__':
    # print(func(*list))
    # print(func_1(*list))
    # print(func_1(3,4,2,3,2,3,4))
    # print(func_2("122","2323","ewewe"))
    # print(func_3(1,2,3,4,5))
    print(sum([1,2,3,4,4,4]))




