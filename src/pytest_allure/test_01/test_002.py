#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26
import os

from py.path import local


def func(x):
    return x+1

def test_func():
    assert func(3)==5


class TestClass(object):
    def test_one(self):
        x="this"
        assert "h" in x
    def test_two(self):
        x="hello"
        assert hasattr(x,"check")

