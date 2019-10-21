# coding:utf-8
__author__ = 'Minn'

import unittest
from src.pages.SignIn import Signin


class test_Signin(unittest.TestCase):
    def test(self):
        sig = Signin()
        sig.Signin(96396311, 11223344)


if __name__ == '__main__':
    test_Signin().test()
