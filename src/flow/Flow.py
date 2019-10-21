# coding:utf-8
__author__ = 'Minn'

'''
    这是一个封装重复操作流程的类，给主要业务流调用
'''
from src.common.Base import Base
from time import sleep


class Flow(Base):
    # 注册
    def signin(self, Account, Password):

        self.WaitElement("text=English")
        self.ClickElement("text=Next")

        # switch to H5
        self.SwitchH5()

        self.ClickElement("xpath=//div[@class=\"tng-button white-green\"]")
        sleep(1)

        # input account info
        self.InputText("xpath=//input[@class=\"mainInput\"]", Account)
        self.driver.hide_keyboard()
        sleep(1)

        # click next button
        self.ClickElement("xpath=//div[@class=\"nextBtn\"]")
        self.SwitchApp()
        sleep(1)

        self.ClickElement("text=I Agree")

        self.VerificationCode()
        sleep(1)

        # self.ClickElement("class=android.widget.EditText")
        self.InputText("class=android.widget.EditText", Password)
        self.ClickElement("text=Next")
        sleep(1)

        # self.ClickElement("class=android.widget.EditText")
        self.InputText("class=android.widget.EditText", Password)
        self.ClickElement("text=Next")
        sleep(2)

        # 填写PIN码
        self.PINCode("000000")
        sleep(1)
        self.PINCode("000000")

        # 接受协议
        self.WaitElement("class=android.widget.CheckBox")
        self.ClickElement("class=android.widget.CheckBox")
        self.ClickElement("text=Agree")
        sleep(2)

        # 点击Confirm按钮
        self.ClickElement("text=Confirm")

        # 关闭广告
        self.CloseAd()

        '''
        # 输入电话号码，点击“Next”按钮
        self.InputText("class=android.widget.EditText", Account)
        self.ClickElement("text=Next")
        sleep(2)

        # 接受协议
        self.ClickElement("text=I Agree")
        sleep(2)

        # 填写验证码
        self.WaitElement("android.widget.EditText", "className")
        self.VerificationCode("class=android.widget.EditText")
        sleep(2)

        # 输入密码，点击“Next”按钮
        self.ClickElement("class=android.widget.EditText")
        self.InputText("class=android.widget.EditText", Password)
        self.ClickElement("text=Next")
        sleep(2)

        # 确认密码，点击“Next”按钮
        self.ClickElement("class=android.widget.EditText")
        self.InputText("class=android.widget.EditText", Password)
        self.ClickElement("text=Next")
        sleep(2)

        # 填写PIN码
        self.PINCode("000000")
        sleep(1)
        self.PINCode("000000")

        # 接受协议
        self.WaitElement("android.widget.CheckBox", "className")
        self.ClickElement("class=android.widget.CheckBox")
        self.ClickElement("text=Agree")
        sleep(2)

        # 点击Confirm按钮
        self.ClickElement("text=Confirm")
        sleep(8)

        # 关闭广告
        # self.WaitElement("android.widget.Image", "className")
        self.ClickElement("class=android.widget.Image")
    '''

    # 登录
    def login(self, Account="96300002", Password="11223344"):
        # 等待元素English的出现，等待时间最大为60秒，60后不出现English这个元素的话就超时
        self.WaitElement("text=English")
        self.ClickElement("text=Next")

        # switch to H5
        self.SwitchH5()

        # click TNG Number button
        self.ClickElement("xpath=//div[@class='tng-button green-fill']")
        sleep(1)

        # input user account
        self.InputText("xpath=//input[@class=\"mainInput\"]", Account)
        self.driver.hide_keyboard()

        # click the next button
        self.ClickElement("xpath=//div[@class=\"nextBtn\"]")
        sleep(1)

        # input password
        self.InputText("xpath=//input[@class=\"mainInput\"]", Password)
        self.driver.hide_keyboard()

        # click the next button
        self.ClickElement("xpath=//div[@class=\"nextBtn\"]")

        # switch to APP
        self.SwitchApp()

        # wait Continue button and click
        self.WaitElement("text=Continue")
        self.ClickElement("text=Continue")

        # input verification code
        self.VerificationCode()

        # Wait CheckBox and select,and click the Agree button
        self.WaitElement("class=android.widget.CheckBox")
        self.ClickElement("class=android.widget.CheckBox")
        self.ClickElement("text=Agree")

        # 闭关广告页面
        self.CloseAd()

    def CloseAd(self):
        sleep(8)
        # self.ClickElement("class=android.widget.Image")
        self.OnClick(0.5, 0.5)

    # 退出登录
    def logout(self):
        sleep(5)
        # 点击My
        self.ClickElement("text=tng4.0_Landing_Icon_My")
        sleep(5)
        # 点击My Account
        self.ClickElement("text=My Account")
        sleep(3)
        '''
        # 向上滑动三次
        self.SwipeUptoLast()
        '''
        print("加载退出页面")
        sleep(5)
        self.SwipetoElement("tng4.0_Wal.Profile_remove_ac")

        # 点击Secure Logout
        self.ClickElement("text=tng4.0_Wal.Profile_remove_ac")
        sleep(2)

        # 点击Logout
        self.ClickElement("text=Logout")
        sleep(5)
        self.driver.quit()

    # 转账
    def TransferMoney(self, user="天字12号"):
        # 点击Pay
        self.ClickElement("text=tng4.0_common_icon_pay")
        sleep(2)

        # 点击Transfer Money
        self.ClickElement("text=Transfer Money")

        # 等待页面元素Later的出现，再点击
        self.WaitElement("text=Later")
        # 点击Later
        self.ClickElement("text=Later")
        sleep(2)

        # 选择用户
        self.ClickElement("text=" + user)

        # 等待页面元素Skip的出现，再点击
        self.WaitElement("text=Skip")
        self.ClickElement("text=Skip")
        sleep(1)

    # 选择Pay方式
    def PayuyMethod(self, method='P2P'):
        self.ClickElement(method)
        if method == "Transfer to Bank":
            self.ClickElement("text=Transfer to Bank")
            self.OnClick(0.5, 0.312)

            print("Transfer to Bank流程暂时还没写自动化测试脚本，退出本次运行！")
            self.driver.quit()
        elif method == "P2P":
            # self.ClickElement("xpath=//div[@class=\"ui_main\"]/div[2]/div")
            self.OnClick(0.25, 0.562)
        elif method == "text=Pick up Cash Overseas":
            self.ClickElement("text=Pick up Cash Overseas")

    # Transfer P2P
    def transfer(self):
        # call login flow
        self.login()
        # 闭关广告页面
        # self.CloseAd()

        # call Transfer Money flow
        self.TransferMoney()
        sleep(2)
        # call input amount flow
        self.WaitElement("text=0.00")
        self.InputAmount()
        sleep(2)
        # self.PayMethod()
        self.ClickElement("text=P2P Transfer")
        self.WaitElement("text=Payment Summary")
        self.ComfirmSummary()
        sleep(3)

    # Schedule Payment
    def SchPay(self, Paymethod):
        self.WaitElement("text=Transfer to Friend")
        sleep(3)
        self.InputAmount(2)
        if Paymethod is "ThankYouPage":
            self.WaitElement("text=Payment Summary")
        elif Paymethod is "AH":
            self.WaitElement("text=Summary")
        sleep(1)
        self.SwipeUptoLast()
        sleep(1)
        self.ClickElement("text=Next Step:")
        sleep(2)
        self.SetSchedule("text=Just once")

    # set Schedule Payment
    def SetSchedule(self, locator):
        self.ClickElement(locator)
        sleep(2)
        _locatorvalue = self._get_locator(locator)[1]
        if _locatorvalue == "Just once":
            self.OnClick()
            sleep(2)
            self.OnClick()
            sleep(2)
            self.PINCode("000000")
        elif _locatorvalue == "Repeat regularly":
            pass

    # Upgrade
    def UpGrade(self):

        # self.CloseAd()
        self.ClickElement("text=Upgrade")

        # wait Membership Upgrade page loading
        self.WaitElement("text=Membership Upgrade")

        # swipe up to last
        self.SwipeUptoLast(3)
        sleep(1)

    # take a picture
    def TakePhoto(self):
        self.ClickElement("id=btn_ok")
        sleep(2)
        self.ClickElement("id=btn_confirm")
        sleep(3)

    def SelectNationality(self, Nationality="PHP"):
        self.WaitElement("text=Other Currency")
        self.ClickElement("text=Other Currency")
        sleep(2)
        self.ClickElement("text=tng4.0_common_flag_" + Nationality + "")

    def GlobalRemittance(self):
        self.WaitElement("text=Cash Pick-up")
        self.ClickElement("text=Select Cash Pick-up Network")
        sleep(1)
        self.ClickElement("xpath=//*[@class='android.widget.CheckedTextView' and @index='1']")
        sleep(1)
        self.InputText("text=Include Middle Name if any", "This is test data")
        self.driver.hide_keyboard()
        sleep(1)
        self.InputText(
            "xpath=//*[@class='android.view.View' and @index='4']/android.view.View/android.view.View[2]/android.widget.EditText",
            "This is test data")
        self.driver.hide_keyboard()
        sleep(1)
        self.SwipeUptoLast(2)
        self.InputText(
            "xpath=//*[@class='android.view.View' and @index='6']/android.view.View[2]/android.view.View[2]/android.widget.EditText",
            85285252)
        self.driver.hide_keyboard()
        sleep(1)
        self.ClickElement("xpath=//*[@class='android.view.View' and @index='7']/android.view.View/android.view.View[2]")
        sleep(1)
        self.ClickElement("xpath=//*[@class='android.widget.CheckedTextView' and @index='1']")
        sleep(1)
        self.ClickElement("xpath=//*[@class='android.view.View' and @index='8']/android.view.View/android.view.View[2]")
        sleep(1)
        self.ClickElement("xpath=//*[@class='android.widget.CheckedTextView' and @index='1']")
        sleep(1)
        self.ClickElement("xpath=//*[@class='android.view.View' and @index='9']/android.view.View/android.view.View[2]")
        sleep(1)
        self.ClickElement("xpath=//*[@class='android.widget.CheckedTextView' and @index='1']")
        self.OnClick()

    def ComfirmSummary(self):
        self.OnClick()
        sleep(2)
        self.PINCode("000000")
