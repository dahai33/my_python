#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26

def reverse(string):
    return string[::-1]

def test_reverse():
    string="good"
    assert reverse(string)=="doog"

    another_string="itest"
    assert  reverse(another_string)=="tseti"

def f():
    return 3

def test_f():
    assert f()==3