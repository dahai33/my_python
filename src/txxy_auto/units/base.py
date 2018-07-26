#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 14:33
from src.txxy_auto.units.drive import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.txxy_auto.units.log import Log as log
import selenium.common.exceptions
import traceback


class base:

    t=5

    def __init__(self):

        self.driver = Driver().get_driver()


    def By_id(self, *loc):

        try:
            WebDriverWait(self.driver,self.t).until(EC.presence_of_all_elements_located(loc))
            return self.driver.find_element_by_id(*loc)
        except selenium.common.exceptions.TimeoutException:
            log.error(traceback.format_exc())
            return False
        except selenium.common.exceptions.NoSuchElementException:
            log.error(traceback.format_exc())
            return False

    def By_Class_name(self,*loc):
        try:
            WebDriverWait(self.driver,self.t).until(EC.presence_of_all_elements_located(loc))
            return self.driver.find_element_by_class_name(*loc)
        except selenium.common.exceptions.TimeoutException:
            log.error(traceback.format_exc())
            return False
        except selenium.common.exceptions.NoSuchElementException:
            log.error(traceback.format_exc())
            return False

    def By_name(self,*loc):
        try:
            WebDriverWait(self.driver,self.t).until(EC.presence_of_all_elements_located(loc))
            return self.driver.find_element_by_name(*loc)
        except selenium.common.exceptions.TimeoutException:
            log.error(traceback.format_exc())
            return False
        except selenium.common.exceptions.NoSuchElementException:
            log.error(traceback.format_exc())
            return False

    def By_Xpath(self,*loc):
        try:
            WebDriverWait(self.driver,t).until(EC.presence_of_all_elements_located(loc))
            return self.driver.find_element_by_name(*loc)
        except selenium.common.exceptions.TimeoutException:
            log.error(traceback.format_exc())
            return False
        except selenium.common.exceptions.NoSuchElementException:
            log.error(traceback.format_exc())
            return False
