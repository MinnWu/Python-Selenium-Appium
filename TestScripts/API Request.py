# coding:utf-8
from selenium import webdriver


def OpenBrowser( url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver

OpenBrowser('https://www.baidu.com')