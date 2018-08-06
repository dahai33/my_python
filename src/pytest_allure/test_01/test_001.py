#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26
import os

import allure

@allure.feature("第一个测试")
def func(x):
    return x+1
@allure.feature("is the test")
def test_func():
    assert func(3)==5

@allure.feature("这是测试类")
class TestClass(object):
    @allure.story("开始测试")
    def test_one(self):
        x="this"
        with allure.step("tttt"):
            allure.attach("函数测试中")
        assert "h" in x
        with allure.step("第二个函数"):
            allure.attach("tjos os ")
    @allure.story("类中第二个函数")
    def test_two(self):
        x="hello"
        assert hasattr(x,"check")
