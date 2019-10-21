# coding:utf-8
__author__ = 'Minn'

from src.flow.Flow import Flow


class Logout(Flow):

    # 退出登录
    def Logout(self):
        self.logout()


if __name__ == '__main__':
    Logout().Logout()
