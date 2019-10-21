# coding:utf-8
__author__ = 'Minn'

from src.flow.Flow import Flow


class Transfer(Flow):

    def Transfer(self):
        self.transfer()
        self.driver.quit()


if __name__ == "__main__":
    Transfer().Transfer()
