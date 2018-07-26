#!/usr/bin/python3
# Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 20:21

from appium import webdriver
from src.txxy_auto.units.log import Log as log
import os
import traceback




class Driver:
    driver = None
    print (driver)

    def get_driver(self):
        try:
            if not Driver().driver:
                self.desired_caps = {}
                self.desired_caps['platformName'] = 'Android'
                self.desired_caps['platformVersion'] = '6.0'
                self.desired_caps['deviceName'] = 'Android Emulator'
                self.desired_caps['appPackage'] = 'com.pycredit.txxy'
                self.desired_caps['appActivity'] = '.StartupActivity'
                self.desired_caps['udid'] = 'SJE5T17823004781'
                self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
                return self.driver
            else:
                return self.driver
        except:
            log.error(traceback.format_exc())

# desired_caps['app'] = (r'../../../sample-code/apps/ContactManager/ContactManager.apk')
# desired_caps['app'] =str(os.path.basename("D:\Object\my_python1\src\auto_test\apk\ApiDemos-debug.apk"))
