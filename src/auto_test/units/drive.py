#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 20:21

from appium import webdriver
import os

class Driver:
    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['app'] = (r'../../../sample-code/apps/ContactManager/ContactManager.apk')
        #desired_caps['app'] =str(os.path.basename("D:\Object\my_python1\src\auto_test\apk\ApiDemos-debug.apk"))
        desired_caps['appPackage'] = 'com.pycredit.txxy'
        desired_caps['appActivity'] = '.StartupActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return self.driver
