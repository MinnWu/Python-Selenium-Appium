# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


class UpGrade(object):
    def __init__(self):
        self.OpenBrowser('http://10.0.50.106/dev4/login/')
        self.KYCLogin()
        sleep(4)

    def Upgrade(self, Text):
        # 通过参数来判断升级VIP还是SVIP
        if Text == 'VIP ID':
            self.DataEntry(Text)
            sleep(2)
            self.Validation(Text)
            sleep(2)
        elif Text == 'SVIP MAIN ID':
            self.DataEntry(Text)
            sleep(2)
            self.Validation(Text)
            sleep(2)
            self.DataEntry('SVIP Alt ID')
            sleep(2)
            self.Validation('SVIP Alt ID')
            sleep(2)
            self.Validation('Add Proof')
            sleep(2)
            self.Validation('Income Information')
            sleep(2)
            self.Compliance('Income Information')
            sleep(2)
        # self.Logout()

    def OpenBrowser(self, url):
        print('打开浏览器；')
        self.driver = webdriver.Chrome()
        # print('窗口最大化；')
        # self.driver.maximize_window()
        print('输入地址；')
        self.driver.get(url)
        return self.driver

    def KYCLogin(self, Account='super', Password='12345678'):
        print('输入用户名；')
        self.InputText('//*[@id="login-username"]', Account)
        sleep(3)
        print('输入密码；')
        self.InputText('//*[@id="login-password"]', Password)
        sleep(3)
        print('点击登录；')
        self.ClickElement('//*[@id="login"]/div[2]/a')

    def Logout(self):
        self.ClickElement('//div[@id="header-options"]/a')
        sleep(3)
        self.ClickElement('//div[@id="header-options"]/ul/li')
        sleep(3)
        self.driver.quit()

    def DataEntry(self, Text):
        print('点击DataEntry；')
        self.ClickElement('//*[@id="header-nav"]/li[1]/a')
        sleep(3)
        if Text == 'VIP ID':
            print('点击VIP ID；')
            self.ClickElement('//*[@id="sourceList-vipId"]')
        elif Text == 'SVIP MAIN ID':
            print('点击SVIP MAIN ID；')
            self.ClickElement('//*[@id="sourceList-svipId"]')
        elif Text == 'SVIP Alt ID':
            print('点击SVIP Alt ID；')
            self.ClickElement('//*[@id="sourceList-svipAltId"]')
        elif Text == 'Add Proof':
            print('点击Add Proof；')
            self.ClickElement('//*[@id="sourceList-addr"]')
        sleep(2)
        print('点击Submit Date Time让列表的数据按倒序排序；')
        self.ClickElement('//*[@id="CREATE_DATETIME"]')
        sleep(2)
        print('点击详情；')
        self.ClickElement('//*[@id="sourceList-table"]/tbody/tr[1]/td[11]/a/span')
        sleep(5)
        if Text == 'Add Proof':
            sleep(4)
            self.InputText('//*[@id="documentInfo-ADDR-addrresidential"]', 'This is Test Data!')
            sleep(1)
            print('输入生日；')
            self.InputText('//*[@id="documentInfo-ADDR-issuranceDate"]', '1990/02/07')
        else:
            hkid = self.HKID()
            if Text == 'SVIP Alt ID':
                print('点击下拉菜单控件；')
                self.ClickElement('//*[@id="documentInfo-AID-idtype"]')
                sleep(1)
                print('选择HKID；')
                self.ClickElement('//*[@id="documentInfo-AID-idtype"]/option[2]')
                sleep(1)
                print('输入HKID；')
                self.InputText('//*[@id="documentInfo-AID-idno"]', hkid)
                sleep(1)
                print('点击下拉菜单控件；')
                self.ClickElement('//*[@id="documentInfo-AID-hkpermresident"]')
                sleep(1)
                print('选择Yes；')
                self.ClickElement('//*[@id="documentInfo-AID-hkpermresident"]/option[2]')
                sleep(1)
                print('点击下拉菜单控件；')
                self.ClickElement('//*[@id="documentInfo-AID-nationality"]')
                sleep(1)
                print('选择HongKong；')
                self.ClickElement('//*[@id="documentInfo-AID-nationality"]/option[102]')
            else:
                print('点击下拉菜单控件；')
                self.ClickElement('//*[@id="documentInfo-PID-idtype"]')
                sleep(1)
                print('选择HKID；')
                self.ClickElement('//*[@id="documentInfo-PID-idtype"]/option[2]')
                sleep(1)
                print('输入HKID；')
                self.InputText('//*[@id="documentInfo-PID-idno"]', hkid)
                sleep(1)
                print('点击下拉菜单控件；')
                self.ClickElement('//*[@id="documentInfo-PID-hkpermresident"]')
                sleep(1)
                print('选择Yes；')
                self.ClickElement('//*[@id="documentInfo-PID-hkpermresident"]/option[2]')
                sleep(1)
                print('点击下拉菜单控件；')
                self.ClickElement('//*[@id="documentInfo-PID-nationality"]')
                sleep(1)
                print('选择HongKong；')
                self.ClickElement('//*[@id="documentInfo-PID-nationality"]/option[102]')
                sleep(1)
                print('输入名字；')
                self.InputText('//*[@id="documentInfo-PI-namesurnameen"]', 'Minn')
                sleep(1)
                print('输入姓氏；')
                self.InputText('//*[@id="documentInfo-PI-namegivennameen"]', 'Wu')
                sleep(1)
                print('点击下拉菜单控件；')
                self.ClickElement('//*[@id="documentInfo-PI-genderopts"]')
                sleep(1)
                print('选择male；')
                self.ClickElement('//*[@id="documentInfo-PI-genderopts"]/option[2]')
                sleep(1)
                print('输入生日；')
                self.InputText('//*[@id="documentInfo-PI-dob"]', '1990/02/07')
            sleep(1)
        print('点击提交；')
        self.ClickElement('//*[@id="documentInfoButton"]')
        sleep(3)

    def Validation(self, Text):
        print('点击Validation；')
        self.ClickElement('//*[@id="header-nav"]/li[2]/a')
        sleep(2)
        if Text == 'VIP ID':
            print('点击VIP ID；')
            self.ClickElement('//*[@id="approvalList-vipId"]')
        elif Text == 'SVIP MAIN ID':
            print('点击SVIP MAIN ID；')
            self.ClickElement('//*[@id="approvalList-svipId"]')
        elif Text == 'SVIP Alt ID':
            print('点击SVIP Alt ID；')
            self.ClickElement('//*[@id="approvalList-svipAltId"]')
        elif Text == 'Credit Card':
            pass
        elif Text == 'Bank Statement':
            pass
        elif Text == 'Add Proof':
            print('点击Add Proof；')
            self.ClickElement('//*[@id="approvalList-addr"]')
        elif Text == 'Income Information':
            print('点击Income Information；')
            self.ClickElement('//*[@id="approvalList-income"]')
        sleep(3)
        print('点击Submit Date Time让列表的数据按倒序排序；')
        self.ClickElement('//*[@id="CREATE_DATETIME"]')
        sleep(2)
        print('点击详情；')
        self.ClickElement('//*[@id="approvalList-table"]/tbody/tr[1]/td[11]/a/span')
        sleep(5)
        print('点击Submit；')
        self.ClickElement('//*[@id="documentInfoButton"]')
        sleep(3)

    def Compliance(self, Text):
        print('点击Compliance；')
        self.ClickElement('//*[@id="header-nav"]/li[4]/a')
        sleep(2)
        if Text == 'SVIP Nationality':
            self.ClickElement('//*[@id="complianceList-alterId"]')
        elif Text == 'Income Information':
            print('点击Income Information；')
            self.ClickElement('//*[@id="complianceList-occupation"]')
        sleep(8)
        print('点击Submit Date Time让列表的数据按倒序排序；')
        self.ClickElement('//*[@id="CREATE_DATETIME"]')
        sleep(8)
        print('点击详情；')
        self.ClickElement('//*[@id="complianceList-table"]/tbody/tr[1]/td[16]/a/span')
        sleep(3)
        self.ClickAlert('Accept')
        # t.accept()
        sleep(5)
        print('点击Submit；')
        self.ClickElement('//*[@id="documentInfoButton"]')
        sleep(3)

    def HKID(self):
        number = 1231233322
        randomnumber = random.randint(10000, 99999)
        print(randomnumber)
        hkid = number + randomnumber
        print(hkid)
        return hkid

    def ClickElement(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def InputText(self, locator, value):
        self.driver.find_element_by_xpath(locator).send_keys(value)

    def ClickAlert(self, Text):
        alert = self.driver.switch_to.alert
        if alert.text:
            if Text == 'Accept':
                alert.accept()
            elif Text == 'Cancel':
                alert.dismiss()
        else:
            pass

    def CancelRecord(self):
        self.OpenBrowser('http://10.0.50.106/dev4/login/')
        self.KYCLogin()
        sleep(2)
        self.ClickElement('//li[@class="compliance "]')
        sleep(2)
        self.ClickElement('//*[@id="complianceList-occupation"]')
        sleep(5)
        self.ClickElement('//*[@id="CREATE_DATETIME"]')
        sleep(4)
        self.ClickElement('//*[@id="complianceList-table"]/tbody/tr[1]/td[16]/a')
        sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="complianceList-table"]/tbody/tr[1]/td[16]/a').send_keys(Keys.ENTER)
        a = 0
        while a in range(100):
            sleep(6)
            self.ClickElement('//*[@id="onHoldButton"]')
            self.ClickElement('//*[@id="submit_on_hold"]')
            self.driver.find_element_by_xpath('//*[@id="submit_on_hold"]').send_keys(Keys.ENTER)
            a = a + 1


if __name__ == '__main__':
    # UpGrade().Upgrade('SVIP MAIN ID')
    ug = UpGrade()
    i = 1
    while i in range(17):
        ug.Upgrade('SVIP MAIN ID')
        i = i + 1
