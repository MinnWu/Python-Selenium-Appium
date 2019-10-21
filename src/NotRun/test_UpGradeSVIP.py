# coding:utf-8
__author__ = 'Minn'

import unittest
from src.pages.UpGradeSVIP import UpGradeSVIP


class test_UpGradeSVIP(unittest.TestCase):
    def test(self):
        spa = UpGradeSVIP()
        for i in range(10):
            spa.UpGradeSVIP('7575837' + str(i), '12345678')


if __name__ == '__main__':
    test_UpGradeSVIP().test()
