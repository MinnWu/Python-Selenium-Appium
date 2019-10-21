# coding:utf-8
__author__ = 'Minn'

'''
    //这是一个自定义函数基础类,里面重写了一些操作动作方法，给后面的业务处理页面调用
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.common.by import By
from config.config import *
# from src.common.GetDriver import driver
from appium import webdriver


class Base(object):
    '''
        # 'noReset': True,  设置不用每次都登录
        # WUJ01JN0TW 这是索尼手机，版本6.0
        # LGH81868ba33ec 这是LG手机，版本5.1
        # 09d8a2910b97fc63 这是LG手机，版本6.0
    '''

    # 初始化时启动APP，获取driver传给其他自定义函数调用
    def __init__(self):

        # import os
        # os.system("start /b appium")

        self.desired_caps = {'platformName': 'Android', 'platformVersion': '5.1',
                             'deviceName': 'LGH81868ba33ec',
                             # 'noReset': True,
                             'appPackage': 'com.sinodynamic.tng.consumer.reg',
                             'appActivity': 'com.sinodynamic.tng.consumer.view.modern.versatile.VersatileActivity'}

        # 打开App
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    # 重写点击元素事件
    def ClickElement(self, locator):
        _locatortype = self._get_locator(locator)[0]
        _locatorvalue = self._get_locator(locator)[1]
        try:
            if _locatortype == "xpath":
                self.driver.find_element(By.XPATH, _locatorvalue).click()
            elif _locatortype == "class":
                self.driver.find_element(By.CLASS_NAME, _locatorvalue).click()
            elif _locatortype == "text":
                self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().text("' + _locatorvalue + '")').click()
            elif _locatortype == "id":
                self.driver.find_element(By.ID, _locatorvalue).click()
        except:
            self.GetScreenShot()
            self.driver.quit()

    # 重写Input text功能
    def InputText(self, locator, value):
        # 分割Locator信息
        _locatortype = self._get_locator(locator)[0]
        _locatorvalue = self._get_locator(locator)[1]
        try:
            if _locatortype == "xpath":
                self.driver.find_element(By.XPATH, _locatorvalue).send_keys(value)
            elif _locatortype == "class":
                self.driver.find_element(By.CLASS_NAME, _locatorvalue).send_keys(value)
            elif _locatortype == "text":
                self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().text("' + _locatorvalue + '")').send_keys(
                    value)
            elif _locatortype == "id":
                self.driver.find_element(By.ID, _locatorvalue).send_keys(value)
        except:
            print("An Element Not Find Of:" + locator)
            self.GetScreenShot()
            self.driver.quit()

    # 重写截图功能
    def GetScreenShot(self):
        import time
        # 截图保存路径
        _image_path = project_path + "\\image\\"
        _timenow = time.strftime('%Y%m%d%H%S', time.localtime())
        _image_name = _image_path + _timenow + ".png"
        self.driver.get_screenshot_as_file(_image_name)
        '''
        # 因为有时候在WebView下无法使用get_screenshot_as_file()进行截图，所有得做一个切换

        if self.driver.current_context == "NATIVE_APP":
            self.driver.get_screenshot_as_file(_image_name)
        else:
            self.SwitchApp()
            self.driver.get_screenshot_as_file(_image_name)
        '''

    # 分解元素位置信息
    # 分割Locator信息..split('=') 以"="号进行分割字符串并放入一个list()内；strip()用于移除字符串头尾指定的字符（默认为空格）另外还有 strip('需要移除的符号')
    def _get_locator(self, locator):
        _locator = locator.split("=", 1)
        _locatortype = _locator[0].strip()
        _locatorvalue = _locator[1].strip()
        return _locatortype, _locatorvalue

    '''
        # 判断该元素是否被加载在DOM中，并不代表该元素一定可见
        # 判断元素(定位后)是否可见
        #  WebDriverWait(driver,5).until(ExpectedConditions.visibilityOf(driver.findElement(By.xpath("//*[@id='kw']"))))
        #  //判断元素是否可见（非隐藏，并且元素的宽和高都不等以0）
        #  WebDriverWait(driver,5).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id='kw']")))
        #  elementToBeClickable(By locator)：判断某个元素中是否可见并且是enable的，这样的话才叫clickable；
        # self.__element = WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(By.XPATH(self.__locatorvalue)))
    '''

    # 重写等待元素函数
    def WaitElement(self, locator, time=60):
        try:
            _locatortype = self._get_locator(locator)[0]
            _locatorvalue = self._get_locator(locator)[1]
            if _locatortype == "class":
                _element = WebDriverWait(self.driver, time).until(
                    lambda x: x.find_element_by_android_uiautomator(
                        'new UiSelector().className("' + _locatorvalue + '")'))
                return _element
            elif _locatortype == "text":
                _element = WebDriverWait(self.driver, time).until(
                    lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("' + _locatorvalue + '")'))
                return _element
            elif _locatortype == "xpath":
                _element = WebDriverWait(self.driver, time).until(
                    lambda x: x.find_element(By.XPATH, value=_locatorvalue))
                return _element
        except:
            print("An Element Not Find Of:" + locator)
            self.GetScreenShot()
            self.driver.quit()

    # 判断页面是否已显示某个元素
    def IfShowElement(self, locator):
        _locatortype = self._get_locator(locator)[0]
        _locatorvalue = self._get_locator(locator)[1]
        try:
            if _locatortype == 'xpath':
                if self.driver.find_element_by_xpath(_locatorvalue).is_displayed():
                    return True
                else:
                    return False
            elif _locatorvalue == 'class':
                if self.driver.find_element_by_class_name(_locatorvalue).is_displayed():
                    return True
                else:
                    return False
            elif _locatortype == 'text':
                if self.driver.find_element_by_android_uiautomator(
                        'new UiSelector().text("' + _locatorvalue + '")').is_displayed():
                    return True
                else:
                    return False
        except:
            return False

    # 上滑至某个元素的位置
    def SwipetoElement(self, locator):
        from time import sleep
        x = 1
        while x == 1:
            if self.IfShowElement(locator) is not True:
                self.SwipeUp(1000)
                sleep(1)
            else:
                break

    # switch to windows and return a element object
    def SwitchWindows(self, element):
        from time import sleep
        _handles = self.driver.window_handles
        # 一个WebView里面有多个Window,直接切换到最后一个window
        # self.driver.switch_to.window(_handles)
        for handle in _handles:
            self.driver.switch_to.window(handle)
            sleep(1)
            _element = self.GetElement(element)
            if _element is not None:
                return _element
        else:
            self.driver.quit()

    # get element object on page by js
    def GetElement(self, element):
        _element = self.driver.execute_script("return document.querySelector('" + element + "')")
        return _element

    # get text info on page by js
    def GetText(self, text):
        i = 0
        while i in range(100):
            _source = self.driver.execute_script("return document.documentElement.outerHTML;")
            if text in _source:
                print("Can Find Element：" + text)
                print(_source)
                return True
            else:
                i = i + 1
        print("Cannot Find Element：" + text)
        return False

    # 切换到H5页面
    def SwitchH5(self):
        _switch = self.driver.contexts
        self.driver.switch_to.context(_switch[1])  # print self.driver.page_source

    # 切换到APP页面
    def SwitchApp(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

    # touch_tap
    def Touch_tap(self, element):
        TouchActions(self.driver).tap(element).perform()

    # confirm
    # def Confirm(self):
    #     self.OnClick(0.9, 0.95)

    # 根据屏幕百分比坐标来点击屏幕
    def OnClick(self, x1=0.9, y1=0.95):
        x = self.GetSize()[0] * x1
        y = self.GetSize()[1] * y1
        self.driver.tap([(x, y)])

    # 输入验证码
    def VerificationCode(self):
        from time import sleep
        self.WaitElement("text=Please wait a moment")
        sleep(1)
        self.ClickElement("class=android.widget.EditText")
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)

    # 向上滑动到底部
    def SwipeUptoLast(self, n=3):
        i = 0
        while i in range(n):
            self.SwipeUp(300)
            i = i + 1

    # 获取手机屏幕大小
    def GetSize(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return (x, y)

    # 向左滑动
    def SwipeLeft(self, t=500):
        l = self.GetSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[0] * 0.5)
        x2 = int(l[1] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向右滑动
    def SwipeRight(self, t=500):
        l = self.GetSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[0] * 0.5)
        x2 = int(l[1] * 0.95)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向上滑动
    def SwipeUp(self, t=500):
        l = self.GetSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[0] * 0.75)
        y2 = int(l[1] * 0.05)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 向下滑动
    def SwipeDown(self, t=500):
        l = self.GetSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[0] * 0.25)
        y2 = int(l[1] * 0.95)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 数字键
    def InputKey(self, num):
        self.driver.press_keycode(num)

    # 回车键
    def Enter(self):
        self.driver.press_keycode(66)

    # 输入金额
    def InputAmount(self, amount=3):
        try:
            if amount > 0 and amount < 100000:
                for n in str(amount):
                    if n == "0":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[4]/td[2]")
                        self.OnClick(0.375, 0.95)
                    elif n == "1":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[1]/td[1]")
                        self.OnClick(0.125, 0.7)
                    elif n == "2":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[1]/td[2]")
                        self.OnClick(0.375, 0.7)
                    elif n == "3":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[1]/td[3]")
                        self.OnClick(0.625, 0.7)
                    elif n == "4":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[2]/td[1]")
                        self.OnClick(0.125, 0.78)
                    elif n == "5":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[2]/td[2]")
                        self.OnClick(0.375, 0.78)
                    elif n == "6":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[2]/td[3]")
                        self.OnClick(0.625, 0.78)
                    elif n == "7":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[3]/td[1]")
                        self.OnClick(0.125, 0.875)
                    elif n == "8":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[3]/td[2]")
                        self.OnClick(0.375, 0.875)
                    elif n == "9":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[3]/td[3]")
                        self.OnClick(0.625, 0.875)
                    elif n == ".":
                        # self.ClickElement("xpath=//table[@class='keyboard ']/tbody/tr[4]/td[3]")
                        self.OnClick(0.625, 0.95)
            else:
                print("你输入的金额无效！")
            # self.ClickElement("xpath=//td[@class='tool next']")
            self.OnClick(0.875, 0.92)
        except:
            self.driver.quit()

    # 输入PIN码
    def PINCode(self, text):
        if len(text) == 6:
            for n in str(text):
                if n == "1":
                    self.OnClick(0.25, 0.625)
                elif n == "2":
                    self.OnClick(0.5, 0.625)
                elif n == "3":
                    self.OnClick(0.75, 0.625)
                elif n == "4":
                    self.OnClick(0.25, 0.72)
                elif n == "5":
                    self.OnClick(0.5, 0.72)
                elif n == "6":
                    self.OnClick(0.75, 0.72)
                elif n == "7":
                    self.OnClick(0.25, 0.812)
                elif n == "8":
                    self.OnClick(0.5, 0.812)
                elif n == "9":
                    self.OnClick(0.75, 0.812)
                elif n == "0":
                    self.OnClick(0.5, 0.91)
        else:
            print("输入的PIN不是6位数！")
