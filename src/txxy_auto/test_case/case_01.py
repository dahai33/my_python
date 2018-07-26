#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 11:32
import unittest
from src.txxy_auto.pages.shouye import shouye
from src.txxy_auto.pages.page import page





from src.txxy_auto.units.drive import Driver
class case01(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        #self.driver.find_element_by_id("com.pycredit.txxy:id/btn_exp").click()
        # self.driver.find_element_by_id("com.pycredit.txxy:id/homepage_login_btn").click()
        # self.driver.find_element_by_id("com.pycredit.txxy:id/username_et").send_keys("15914089412")
        # self.driver.find_element_by_id("com.pycredit.txxy:id/password_et").send_keys("123456")
        # self.driver.find_element_by_id("com.pycredit.txxy:id/login_btn").click()
        shouye().login()
        page().tear_down()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(case01)
    unittest.TextTestRunner(verbosity=2).run(suite)
