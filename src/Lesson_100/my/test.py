#!/usr/bin/python3
# Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26


import os
import yaml
import configparser


# print(os.path.abspath().join(os.path.basename("__file__")))
# print(os.path.abspath("__file__"))
# print(os.path.basename("_file_"))
# # print(os.path.abspath().join(os.path.basename("test.my")))
# # os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data/config.ini"))
# print(os.path.abspath(os.path.join(os.path.basename(__file__))))
# print(os.path.abspath(os.path.basename(__file__)), os.pardir, "../test/Lesson_01.py")
# print(os.path.abspath(os.path.basename((__file__))))
# print(os.path.abspath(os.path.pardir))
# print(os.path.abspath(os.path.pardir), os.pardir, "my/test.py")
# print(os.path.abspath(os.path.basename(__file__)), os.path.pardir, "../my/test.py")
# print(os.path.abspath(os.path.basename(__file__)), os.path.pardir)
# print(os.path.abspath(os.path.basename(__file__)),os.path.pardir,"/my/test.py")
# print("*************")
# #print(os.path.abspath(os.path.basename(__file__), os.path.pardir,"./test.py"))
# print(os.path.abspath(os.path.basename(__file__)).join(os.path.pardir),"./test.my")
# # print((os.path.abspath(os.path.dirname(__file__))).join("test.my")
# print(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,"./my/test.py")))
# #print(os.path.abspath(os.path.basename(__file__).join(os.path.pardir),"./my/test.py"))
# print(os.path.abspath(os.path.join(os.path.basename(__file__),os.path.pardir,"./my/test.py")))
PATH=lambda p:os.path.abspath(os.path.join(os.path.basename(__file__),os.path.pardir,p))
# print(PATH("../my/
# yaml"))

# f=open(PATH("../my/yaml"))
# dict=yaml.load(f)
# print(dict)
# print("*****")
# print(dict.get("regist"))
# print("_____")
# print(dict.get("regist").get("desc")[0].get("name"))
#print(PATH("../conf.ini/conf.ini"))

#ff=configparser.ConfigParser.read("/Users/apple/Documents/GitHub/my_python/src/Lesson_100/my/conf.ini")
cf = configparser.ConfigParser()
cf.read("conf.ini")
# conf=configparser.ConfigParser().read(PATH("../my/conf.ini"))
# print(cf.sections())
# print(conf.sections())
# print(cf.sections())
# print(cf.)
# secs=cf.sections()
# opts=cf.options("db")

print(cf.get("db","url"))

def get_db(self,are,key):

    value=self.cf.get(are,key)

    print(value)
    return value

print(get_db("db","url"))
print(cf.get("db","url"))


