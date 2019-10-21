# coding:utf-8
__author__ = 'Minn'
from src.flow.Flow import Flow
from time import sleep


class UpGradeVIP(Flow):
    def UpGradeVIP(self):
        # self.signin(Account, Password)
        self.login()

        self.UpGrade()

        # click SVIP button
        self.ClickElement("text=VIP")
        sleep(1)

        self.WaitElement("text=ID Doc Upload")
        self.SwipeUptoLast()

        self.ClickElement("text=Take Photo Now")

        # take a picture
        self.TakePhoto()

        self.WaitElement("text=Click here to retake photo")
        sleep(2)

        self.ClickElement("text=Please select your Nationality")
        sleep(2)
        self.ClickElement("text=China (Hong Kong SAR)")
        sleep(1)

        self.InputText("text=+852", 96300002)
        self.driver.hide_keyboard()

        self.SwipeUptoLast()
        self.OnClick(0.1, 0.84)
        # self.OnClick()
        self.driver.quit()



if __name__ == '__main__':
    UpGradeVIP().UpGradeVIP()
