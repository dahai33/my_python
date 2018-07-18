#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 20:51
import os
# p=os.popen("adb get-serialno")
# l=os.popen("adb devices")
# print(p.read())
# print(l.read())
class window:
    @staticmethod
    def get_devices(cmd):
        dev_list=[]
        p=os.popen(cmd)
        for i in p.read():
            dev_list[i]=p.read().index[i]
        return dev_list

class ADB(object):
    def __init__(self, device_id=""):

        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" % device_id

    def get_device_id(self):
        return os.open("get-serialno").read().strip()