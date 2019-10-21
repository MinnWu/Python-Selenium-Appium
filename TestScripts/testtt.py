# # coding:utf-8
from selenium import webdriver
# #
# # mobileEmulation = {'deviceName': 'iPhone X'}
# # options = webdriver.ChromeOptions()
# # options.add_experimental_option('mobileEmulation', mobileEmulation)
# #
# # driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
# #
# # driver.get('http://m.baidu.com')
#
# # from time import sleep
#
# #
# # def printtext():
# #     print("能看见我就说明调用成功")
#
#
# import xlrd
#
#
# def Open_Excel(FileUrl=r'D:\PycharmProjects\TNG\data\GR_Data.xlsx'):
#     data = xlrd.open_workbook(FileUrl)
#     return data
#
#
# def Get_Sheet_all_data_to_list():
#     data = Open_Excel()
#     Sheet = data.sheet_by_index(0)
#     rownum = Sheet.nrows  # 获取有效数据行数
#     rowlist = Sheet.row_values(0)
#     list = []
#     for j in range(1, rownum):
#         dict = {}
#         for i in range(len(rowlist)):
#             collist = Sheet.col_values(i)
#             dict[rowlist[i]] = collist[j]
#         list.append(dict)
#     return list
#
#
# def Get_Data_to_dict():
#     data = Open_Excel()
#     Sheet = data.sheet_by_index(0)
#     dict = {}
#     Nationality = Sheet.col_values(0)
#     Amount = Sheet.col_values(1)
#     for i in range(1, len(Nationality)):
#         dict[Nationality[i]] = Amount[i]
#     # print(dict)
#     return dict
#
#     # 下面代码是键值对，适用做用户名和密码的参数化
#     # Username = Sheet.col_values(0)
#     # Password = Sheet.col_values(1)
#     # for i in range(1, len(Username)):
#     #     dict[Username[i]] = Password[i]
#     # return dict
#
#
# list = Get_Sheet_all_data_to_list()
# # print(list)
# # dict = Get_Data_to_dict()
# # print(dict)
#
#
# for i in range(len(list)):
#
#     for key, value in list[i].items():
#         print(key + ':' + str(value))

def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi()
print(a)
# outputs: <function greet at 0x7f2143c01500>

# 上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
# 现在试试这个

print(a())