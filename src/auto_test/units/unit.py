#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 20:02
import yaml
import os
from src.auto_test.units.drive import Driver

# driver=Driver.get_driver()
# def Analysis_yaml(self, filepath):
#     path="r"+ self.filepath
#     f = open(path,encoding="utf-8")
#     dic = yaml.load(f)
#     return dic
#
# def By_id(self,*elments):
#
#     drive = Driver().get_driver()
#     drive.find_element_by_id(elments)
#
# def By_xpath(self,*elments):
#     drive=Driver.get_driver()
#     drive.find_element_by_xpath(elments)
#
# def By_class_name(self,*elments):
#     drive = Driver.get_driver()
#     drive.find_element_by_class_name(elments)
#
# def By_xpath(self,*elments):
#     drive=Driver.get_driver()
#     drive.find_element_by_xpath(elments)

# dic=Analysis_yaml(r"D:\Object\my_python1\src\auto_test\page\login_page.yaml")
# print(os.path.dirname())
# f=open(os.path.dirname().join("../page/login_page.yaml"))
# x = yaml.load(f)


f=open(r"D:\Object\my_python1\src\auto_test\page\login_page.yaml",encoding="utf-8")


dic=yaml.load(f)
# dic=Analysis_yaml(filepath)

print(dic.get("LoginPage")[0].get("name"))




