#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26

import pytest

@pytest.fixture(scope="session")
def log_global_env_facts(f):

    if pytest.config.pluginmanager.hasplugin("junitxml"):
        my_juit=getattr(pytest.config,"_xml",None)

    my_juit.add_global_property("arch","ppc")
    my_juit.add_global_property("storage_type","ceph")

@pytest.mark.usefixture(log_global_env_facts.__name__)
def start_and_prepare_env():
    pass

class Testme(object):
    def test_foo(self):
        assert True