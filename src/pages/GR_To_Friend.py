# coding:utf-8

from src.flow.Flow import Flow
from time import sleep
from config.data import Get_Data_to_dict


class GRToFriend(Flow):
    def grtofriend(self):
        dict = Get_Data_to_dict()
        for key, value in dict.items():
            Nationality=key
            Amount=value
            # self.login()
            self.CloseAd()
            self.TransferMoney()
            # self.SwipeUp()
            sleep(3)
            self.SelectNationality(Nationality)
            sleep(1)
            self.InputAmount(Amount)
            self.WaitElement("text=Service Detail")
            sleep(2)
            self.ClickElement("text=Pick up Cash Overseas")
            # sleep(2)
            # self.WaitElement("text=Later")
            # self.ClickElement("text=Later")
            self.GlobalRemittance()
            sleep(2)
            self.ComfirmSummary()
            sleep(2)
            self.OnClick(0.1, 0.95)
        self.driver.quit()


if __name__ == '__main__':
    GR = GRToFriend()
    GR.grtofriend()
