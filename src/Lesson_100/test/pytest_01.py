#!/usr/bin/python3
#Author:刘海涛
# --*-- coding: uft-8 --*--
# @Time   : 16:26
import pytest
# fixture函数可以使用在测试函数中，测试类中，测试文件中以及整个测试工程中。
# fixture支持模块化，fixture可以相互嵌套
# fixture支持参数化
# fixture支持unittest类型的setup和teardown


class TestClass:
    # def func(x):
    #     return x + 1
    #
    # def test_func(self):
    #     assert self.func(4) == 5

    def test_one(self):
        assert "h" in "this"

    # def test_two(self):
    #     x="hello"
    #     assert hasattr(x,"hello",400)
    # def test_zero_di(self):
    #     with pytest.raises(ZeroDivisionError) as excinfo:
    #
    #         1/0
    #     assert excinfo.type == 'RuntimeError'
