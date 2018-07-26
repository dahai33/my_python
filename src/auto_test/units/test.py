#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 15:40
import src.auto_test.units.tools as t
devid=t.devices_id()
print(devid.get_device_id()[0])