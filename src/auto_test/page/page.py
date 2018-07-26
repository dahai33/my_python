#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26
from appium import webdriver
import unittest
import sys
import selenium.common.exceptions
import src.auto_test.units.log as log
from selenium.webdriver.support.wait import WebDriverWait
from src.auto_test.units.drive import Driver
import traceback
from selenium.webdriver.support import expected_conditions as EC
class Page():
    def __init__(self):
        driver=Driver.get_driver()


    def click(self,element_id):
        driver = Driver.get_driver()
        driver.find_element_by_class_name("nam_id").click()

    def By_id(self,*element):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(element))
            return self.driver.find_element(*element)
        except selenium.common.exceptions.TimeoutException:
            log.error(traceback.format_exc())
            return False
        except selenium.common.exceptions.NoSuchElementException:
            log.error(traceback.format_exc())
            return False
    def By_xpath(self,*element):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(element))
            return self.driver.find_element(*element)
        except selenium.common.exceptions.TimeoutException:
            log.error(traceback.format_exc())
            return False
        except selenium.common.exceptions.NoSuchElementException:
            log.error(traceback.format_exc())
            return False

    def find_selector(self,_id):

        try:
            return self.driver.find_element_by_css_selector(_id)
        except selenium.common.exceptions.TimeoutException:
            log.error(traceback.format_exc())
            return False
        except selenium.common.exceptions.NoSuchElementException:
            log.error(traceback.format_exc())
            return False

    def send_keys(self,value,*loc):

        try:
            #self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            log.error(traceback.format_exc())
            raise e










