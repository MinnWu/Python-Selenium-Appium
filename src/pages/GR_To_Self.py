# coding:utf-8

from src.flow.Flow import Flow
from time import sleep


class GRToSelf(Flow):
    def grtoself(self):
        self.login()
        self.TransferMoney()
        # self.SwipeUp()
        sleep(1)
        self.SelectCountry("PHP")
        sleep(1)
        self.InputAmount(100)
        self.WaitElement("text=Service Detail")
        sleep(2)
        self.ClickElement("text=Pick up Cash Overseas")
        # sleep(2)
        # self.WaitElement("text=Later")
        # self.ClickElement("text=Later")
        self.GlobalRemittance()
        sleep(2)
        self.ComfirmSummary()


if __name__ == '__main__':
    GR = GRToSelf()
    GR.grtoself()
