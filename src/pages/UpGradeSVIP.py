# coding:utf-8
__author__ = 'Minn'

from src.flow.Flow import Flow
from src.pages.UpGradeFromKYC import UpGrade
from time import sleep


class UpGradeSVIP(Flow):
    def UpGradeSVIP(self, account, password):
        self.login(account, password)
        self.UpGrade()

        # click SVIP button
        self.ClickElement("text=SVIP")
        sleep(1)

        # click confirm
        self.OnClick()
        sleep(1)

        # swipe up to last
        self.SwipeUptoLast(5)

        # switch to H5
        self.SwitchH5()

        # get element by switch to windows
        _element = self.SwitchWindows(".checkbox")

        # click checkbox
        self.Touch_tap(_element)

        # click confirm button
        self.Touch_tap(self.GetElement(".control.right.tick.no-bg.green"))
        sleep(1)

        # input password
        self.InputText("xpath=//div[@class=\"container\"]/input", 12345678)
        self.driver.hide_keyboard()

        # click confirm button
        self.Touch_tap(self.GetElement(".control.right.tick.no-bg.green"))
        sleep(1)

        # switch to APP
        self.SwitchApp()

        # input verification code
        self.VerificationCode()
        sleep(1)

        self.WaitElement("text=ID Doc Upload")
        self.SwipeUptoLast()
        sleep(1)
        self.ClickElement("text=Take Photo Now")

        # click Next Step button
        # self.WaitElement("text=Next Step")
        # sleep(2)
        # self.ClickElement("text=Next Step")

        self.TakePhoto()

        self.WaitElement("text=Next Step")
        sleep(2)
        # click Next Step button
        self.ClickElement("text=Next Step")

        self.TakePhoto()

        self.WaitElement("text=Next Step")
        sleep(2)
        # click Next Step button
        self.ClickElement("text=Next Step")

        # wait residential address page loading and input information
        self.WaitElement("text=Residential Address")
        sleep(3)
        self.ClickElement("text=Please select Country")
        sleep(2)
        self.ClickElement("text=China (Hong Kong SAR)")
        sleep(1)
        self.ClickElement("text=Please select Region")
        sleep(2)
        self.ClickElement("text=Hong Kong Island")
        sleep(1)
        self.InputText(
            "xpath=//*[@class='android.view.View' and @index='6']/android.view.View[2]/android.widget.EditText",
            "This is test data")
        self.driver.hide_keyboard()
        self.InputText(
            "xpath=//*[@class='android.view.View' and @index='7']/android.view.View[2]/android.widget.EditText",
            "This is test data")
        self.driver.hide_keyboard()
        self.ClickElement("text=Next Step")
        self.WaitElement("text=Your Own Total Income")
        sleep(2)
        self.ClickElement("text=Please select your own investment income")
        sleep(2)
        self.ClickElement("xpath=//*[@class='android.widget.CheckedTextView' and @index='3']")
        sleep(2)
        self.ClickElement("text=Please select your own job information")
        sleep(2)
        # self.ClickElement("text='Full-time Employed'")
        self.ClickElement("xpath=//*[@class='android.widget.CheckedTextView' and @index='1']")
        self.InputText("xpath=//*[@class='android.view.View' and @index='8']/android.widget.EditText",
                       "This is test data")
        self.driver.hide_keyboard()
        self.SwipeUp(1000)
        sleep(2)
        self.ClickElement("text=Please select Industry")
        sleep(2)
        self.ClickElement("text=Auctioneer")
        sleep(2)
        self.ClickElement("text=Please select Job Role")
        sleep(2)
        self.ClickElement("text=Middle Management")
        sleep(1)
        self.ClickElement("text=Please state Monthly Job Income")
        sleep(2)
        self.ClickElement("xpath=//*[@class='android.widget.CheckedTextView' and @index='3']")
        self.SwipeUp(1000)
        self.ClickElement("text=Remittance")
        self.SwipeUp(1000)
        self.ClickElement("text=7-Eleven")
        self.SwipeUptoLast()
        # self.ClickElement("text=Next Step")
        self.driver.quit()
        UpGrade().Upgrade('SVIP MAIN ID')


if __name__ == '__main__':
    UpGradeSVIP().UpGradeSVIP()
