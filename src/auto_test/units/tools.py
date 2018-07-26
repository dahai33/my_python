#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 17:38
import os
import src.auto_test.units.log as L
import yaml


class devices_id(object):
     def __init__(self, device_id=""):
         if device_id == "":
             self.device_id = ""
         else:
            self.device_id = "-s %s" % device_id
     @staticmethod
     def get_device_id():
         device_list=[]
         device_list=os.popen("adb get-serialno").read().splitlines()
         return device_list

     @staticmethod
     def install_apk(apk_path):
         if os.popen("adb install" + apk_path):
             L.Log.d(apk_path,"apk包安装成功")
         else:
             L.Log.e(apk_path,"apk安装失败")
     @staticmethod
     def remove_apk(apk_name):
         if os.popen("adb uninstall" + apk_name):
             L.Log.d(apk_name,"apk包卸载成功")
         else:
             L.Log.e(apk_name,"apk包卸载失败")





if __name__=='__main__':

    devices_id.remove_apk("cdd d")
    devices_id.install_apk("d:/cont/cdent/com.tianxianyong.com")
    p=os.popen("adb shell pm list packages moffice_eng").read().splitlines()
    print(p)
