# coding:utf-8
__author__ = 'Minn'

from src.pages.login import Login
import unittest


class Testlogin(unittest.TestCase):

    def test(self):
        lg = Login()
        lg.login()


if __name__ == "__main__":
    Testlogin().test()
