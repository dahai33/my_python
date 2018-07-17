#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26

class Device:
    @staticmethod
    def get_android_devices():
        android_devices_list=[]
        for device in cmd('adb devices').splistlines():
            if 'device' in device and 'devices' not in device:
                device=device.split('\t’)[0]
                android_devices_list.append(device)
        return android_devices_list
