# coding:utf-8
__author__ = 'Minn'

from src.flow.Flow import Flow
from time import sleep


class SchPayAH(Flow):
    def SchPayAH(self):
        # call P2P Transfer flow
        self.transfer()
        self.WaitElement("text=Transaction Completed")
        # self.ClickElement("text=Transaction History")
        self.OnClick(0.5, 0.687)
        self.WaitElement("text=Important Notice")
        sleep(2)
        self.SwipeUptoLast()
        sleep(1)
        self.ClickElement("text=Setup Your Next Transaction")
        self.SchPay("AH")
        self.driver.quit()


if __name__ == "__main__":
    SchPayAH().SchPayAH()
