# coding:utf-8 #设置编码格式

# 引入appium库中和webdriver包
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import os


class Get_driver:
    def get_driver(self):
        # 定义一个desired_caps字典来保存启动APP所需的那5个参数
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1',
                        'deviceName': 'LGH81868ba33ec',
                        'appPackage': 'com.sinodynamic.tng.consumer.reg',
                        'appActivity': 'com.sinodynamic.tng.consumer.view.modern.versatile.VersatileActivity'}

        # 通过webdriver包下面的Remote方法打开App
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return self.driver


class Base_page:
    def __init__(self):
        self.driver = Get_driver.get_driver()

    def WaitElement(self):
        try:
            WebDriverWait(self.driver, 60).until(
                lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("English")'))
        except:
            print("找不到元素")

    def OnClick(self, locator):
        self.driver.find_element(By.XPATH, locator).click()


# driver.find_element_by_android_uiautomator('new UiSelector().text("Next")').click()
# _switch = driver.contexts
# driver.switch_to.context(_switch[1])
# driver.find_element_by_xpath("//div[@class='tng-button green-fill']").click()

pc = input('请输入系统 win or mac：')


def stop_appium(post_num=4723):
    '''关闭appium服务'''
    if pc.upper() == 'WIN':
        p = os.popen(f'netstat  -aon|findstr {post_num}')
        p0 = p.read().strip()
        if p0 != '' and 'LISTENING' in p0:
            p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
            os.popen(f'taskkill /F /PID {p1}')  # 结束进程
            print('appium server已结束')
    elif pc.upper() == 'MAC':
        p = os.popen(f'lsof -i tcp:{post_num}')
        p0 = p.read()
        if p0.strip() != '':
            p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
            os.popen(f'kill {p1}')  # 结束进程
            print('appium server已结束')


def start_appium(post_num=4723):
    '''开启appium服务'''
    stop_appium(post_num)  # 先判断端口是否被占用，如果被占用则关闭该端口号
    # 根据系统，启动对应的服务
    cmd_dict = {
        'WIN': f' start /b appium -a 127.0.0.1 -p {post_num} --log xxx.log --local-timezone ',
        'MAC': f'appium -a 127.0.0.1 -p {post_num} --log xxx.log --local-timezone  & '
    }
    os.system(cmd_dict[pc.upper()])
    sleep(3)  # 等待启动完成
    print('appium启动成功')
