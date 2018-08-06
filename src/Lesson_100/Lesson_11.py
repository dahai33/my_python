#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26

import os

for root,dirs,files in os.walk("/"):
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,dirs)