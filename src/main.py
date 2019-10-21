# coding:utf-8
__author__ = 'Minn'
'''
    //Main方法，设置了运行测试用例，生成测试报告
'''
import unittest, os
import HTMLTestRunner
from config.config import report_name, test_case_path


# def creat_suite():
#     uit = unittest.TestSuite()
#
#     # 获取所有以test开头.py结尾的测试用例文件
#     discover = unittest.defaultTestLoader.discover(test_case_path, pattern="test*.py", top_level_dir=None)
#     # print (discover)
#     # 遍历并执行每一个测试用例
#     for test_suite in discover:
#         for test_case in test_suite:
#             uit.addTest(test_case)
#     return uit

discover = unittest.defaultTestLoader.discover(test_case_path, pattern="test*.py", top_level_dir=None)

# 执行测试
if __name__ == "__main__":
    # suite = creat_suite()
    fb = open(report_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title=u'TNG自动化测试报告', description=u'项目描述：RGE环境')
    runner.run(discover)
    fb.close()
