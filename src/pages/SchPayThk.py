# coding:utf-8
__author__ = 'Minn'

from src.flow.Flow import Flow
from time import sleep


class SchPayThk(Flow):
    def SchPayThk(self):
        # Call P2P Transfer flow
        self.transfer()
        # Wait the button of Setup You Next Transaction and click
        self.WaitElement("text=Setup Your Next Transaction")
        self.ClickElement("text=Setup Your Next Transaction")
        self.SchPay("ThankYouPage")
        self.driver.quit()


if __name__ == "__main__":
    SchPayThk().SchPayThk()
