# coding:utf-8
__author__ = 'Minn'

import unittest
from src.pages.SchPayAH import SchPayAH


class test_SchPayAH(unittest.TestCase):
    def test(self):
        spa = SchPayAH()
        spa.SchPayAH()


if __name__ == '__main__':
    test_SchPayAH().test()
