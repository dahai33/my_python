#!/usr/bin/python3
# Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26

from appium import webdriver

from src.auto_test.android.shouye.page import page

drive = webdriver.Remote("url", "mobile_info")
drive.find_element_by_accessibility_id("name")
drive.seep(2)

class shouye(page):

    login_button = drive.find_element_by_accessibility_id("calss")
    sumbit_button = drive.find_element_by_accessibility_id("class")

    drive.find_element_by_accessibility_id("name").click()


