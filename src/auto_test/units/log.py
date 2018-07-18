#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26

import time
from termcolor import colored,cprint

class Log:
    @staticmethod
    def e(msg,list_msg=[]):
        if list_msg:
            Log.show_list(msg,list_msg,Log.e)
        else:
            Colourlog().show_error(get_now_time()+"[Error]"+"".join(msg))
    @staticmethod
    def w(msg,list_msg=[]):
        if list_msg:
            Log.show_list(msg,list_msg,Log.w)
        else:
            Colourlog().show_warn(get_now_time()+"[warn]"+"".join(msg))
    @staticmethod
    def i(msg,list_msg=[]):
        if list_msg:
            Log.show_list(msg,list_msg,Log.i)
        else:
            Colourlog().show_info(get_now_time()+"[info]"+"".join(msg))

    @staticmethod
    def d(msg,list_msg=[]):
        if list_msg:
            Log.show_list(msg,list_msg,Log.d)
        else:
            Colourlog().show_debug(get_now_time()+"[debug]"+"".join(msg))

    @staticmethod
    def show_list(msg,list_msg,f):
        temp=msg+"["+"\t".join(list_msg)+"]"
        f(temp)


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

class Colourlog:

    @staticmethod
    def c(msg,colour):
        try:
            p=lambda x:cprint(x,'%s' % colour)
            return p(msg)
        except:
            print(msg)

    @staticmethod
    def show_verbose(msg):
        Colourlog().c(msg,"white")

    @staticmethod
    def show_debug(msg):
        Colourlog().c(msg,"blue")

    @staticmethod
    def show_info(msg):
        Colourlog().c(msg,"green")

    @staticmethod
    def show_warm(msg):
        Colourlog().c(msg,"yellow")

    @staticmethod
    def show_error(msg):
        Colourlog().c(msg,"red")


