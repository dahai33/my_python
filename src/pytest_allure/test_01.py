#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26
import os

import pytest
from py.path import local


def func(x):
    return x+1

@pytest.mark.test_id(1901)
def test_func():
    assert func(3)==5


class TestClass(object):
    def test_one(self):
        x="this"
        assert "h" in x
    def test_two(self):
        x="hello"
        assert hasattr(x,"check")
@pytest.fixture()
def smtp_connection():
    import smtplib
    return smtplib.SMTP("SMTP.GMAIL.COM")

def test_smtp(smtp_connection):
    response,msg=smtp_connection.echo()
    assert response==250
    assert 0

