# coding:utf-8
__author__ = 'Minn'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

'''
    设置driver
'''
global driver = Driver()

def Driver():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '7.1.2',
                    'deviceName': '127.0.0.1:62025',
                    # 'noReset': True,
                    'appPackage': 'com.sinodynamic.tng.consumer.reg',
                    'appActivity': 'com.sinodynamic.tng.consumer.view.modern.versatile.VersatileActivity'}

    # 'noReset': True,  设置不用每次都登录
    # WUJ01JN0TW 这是索尼手机，版本6.0
    # LGH81868ba33ec 这是LG手机，版本5.1
    # 09d8a2910b97fc63 这是LG手机，版本6.0

    # 打开App
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


def Outer(function):
    def Inner(*args, **kwargs):
        WaitElement(*args)
        function(*args, **kwargs)  # 业务函数

    return Inner


def WaitElement(Text):
    driver = Driver()
    try:
        WebDriverWait(driver, 60).until(
            lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("' + Text + '")'))
    except:
        print("找不到元素")


class Base:
    def __init__(self):
        self.driver = Driver()

    # @Outer
    def ClickElement(self, Text):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + Text + '")').click()

    # @Outer
    def InputTest(self, locator, Text):
        self.driver.find_element_by_xpath(locator).send_keys(Text)


base = Base()
base.ClickElement("Next")
