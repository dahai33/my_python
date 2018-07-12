#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 19:22
from appium import webdriver
# from unit import android_base
driver=webdriver.Remote("http://localhost:4723://wd/hub",android_base)
driver.find_element_by_name("1").click()
driver.quit()
driver.find_element_by_xpath("/id/class").click()

#安装安卓包
def install_app():
    driver.install_app(("../apk/ApiDemos-debug.apk"))
    driver.install_app("D:\\android\\apk\\ContactManager.apk")

#卸载安卓包
def remove_app():
    driver.remove_app("com.pycredit.txxy")
#关闭引用 关闭到后台
driver.close_app()
#启动应用
driver.launch_app()
##判断引用是否安装
driver.is_app_installed("com.pycredit.txxy")
#将应该至于后台
# driver.runAappInBackGround(2)
driver.background_app(10)
#应该重置
driver.reset()