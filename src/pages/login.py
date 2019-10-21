# coding:utf-8
__author__ = 'Minn'

from src.flow.Flow import Flow

class Login(Flow):
    def Login(self):
        self.login()
        self.driver.quit()


if __name__ == "__main__":
    Login().Login()
