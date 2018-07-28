#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 15:36
import json
json_data=[{"a":1,"b":2,"c":3,"d":4}]
#print(json_data)
dict=json_data[0]
print(dict.get("a"))
print (json.dumps(json_data))