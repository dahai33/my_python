#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 10:49
import os
#PATH=lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))
PATH=lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))
config_path=PATH("../conf/XXX")
class Read_Config:

    def __init__(self):
        fd=open(config_path)
        data=fd.read
