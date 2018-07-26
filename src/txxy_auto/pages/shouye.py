#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 10:24
from src.txxy_auto.units.drive import Driver as driver
from src.txxy_auto.pages.page import page


class shouye(page):



    def login(self):
        # self.driver.find_element_by_id("com.pycredit.txxy:id/btn_exp").click()
        # self.driver.find_element_by_id("com.pycredit.txxy:id/homepage_login_btn").click()
        # self.driver.find_element_by_id("com.pycredit.txxy:id/username_et").send_keys("15914089412")
        # self.driver.find_element_by_id("com.pycredit.txxy:id/password_et").send_keys("123456")
        # self.driver.find_element_by_id("com.pycredit.txxy:id/login_btn").click()
        self.By_id("com.pycredit.txxy:id/btn_exp").click()
        self.By_id("com.pycredit.txxy:id/homepage_login_btn").click()
        self.By_id("com.pycredit.txxy:id/username_et").send_keys("15914089412")
        self.By_id("com.pycredit.txxy:id/password_et").send_keys("123456")
        self.By_id("com.pycredit.txxy:id/login_btn").click()
        if self.assertEqual("id","我的"):
            print("登录成功")
        else:
            print("“登录失败")


    # def regist(self):
    #     self.driver.find_element_by_id("com.pycredit.txxy:id/register_btn").click()
    #     self.driver.find_element_by_id("ccom.pycredit.txxy:id/verifycode_mobileId").send_keys("15914089412")
    #     self.driver.find_element_by_id("com.pycredit.txxy:id/register_password_et").click()
    #     self.driver.find_element_by_id("com.pycredit.txxy:id/verifycode_codeId").send_keys("666666")
    #     self.driver.find_element_by_id("com.pycredit.txxy:id/register_btn").click()







