# coding:utf-8
__author__ = 'Minn'
'''
    //这是注册业务
'''
from src.flow.Flow import Flow


class Signin(Flow):

    def Signin(self, Account, Password):
        self.signin(Account, Password)
        self.driver.quit()  # sys.exit()


if __name__ == '__main__':
    i = 1
    while i in range(10):
        Account = "9639633" + str(i)
        Signin().Signin(Account, "11223344")
        i = i + 1
    # Signin().Signin(96396330, 11223344)
