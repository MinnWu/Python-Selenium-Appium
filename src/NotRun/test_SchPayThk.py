# coding:utf-8
__author__ = 'Minn'

import unittest
from src.pages.SchPayThk import SchPayThk


class test_SchPayThk(unittest.TestCase):
    def test(self):
        spt = SchPayThk()
        spt.SchPayThk()


if __name__ == '__main__':
    test_SchPayThk().test()
