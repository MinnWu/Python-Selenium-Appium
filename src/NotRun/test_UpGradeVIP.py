# coding:utf-8
__author__ = "Minn"

import unittest
from src.pages.UpGradeVIP import UpGradeVIP


class test_UpGradeVIP(unittest.TestCase):
    def test(self):
        ugVIP = UpGradeVIP()
        ugVIP.UpGradeVIP()


if __name__ == '__main__':
    test_UpGradeVIP().test()
