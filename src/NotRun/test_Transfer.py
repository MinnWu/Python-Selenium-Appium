# coding:utf-8
__author__ = 'Minn'

from src.pages.login import Login
from src.pages.Transfer import Transfer
import unittest


class TestTM(unittest.TestCase):

    def test(self):
        # 创建Transfer对象tm,通过tm调用transfer方法
        tm = Transfer()
        tm.transfer()


if __name__ == "__main__":
    TestTM().test()
