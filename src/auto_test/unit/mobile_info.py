#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 18:59

import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class android_base():
    tuple_conf={}
    tuple_conf["platformName"]="Android"
    tuple_conf["platformVersion"]="6.0"
    tuple_conf["deviceName"]="Android Emulator"
    tuple_conf["app"]=PATH("../apk/ApiDemos-debug.apk")

class iso_conf_base():
    list_conf={}
    list_conf["app"]="app"
    list_conf["platformName"]="ios"
    list_conf["platformVersion"]="10.0"
    list_conf["deviceName"]="iPhone 6"

