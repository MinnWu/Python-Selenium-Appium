# coding:utf-8

import xlrd


def Open_Excel(FileUrl):
    data = xlrd.open_workbook(FileUrl)
    return data


def Get_Data_to_dict():
    data = Open_Excel()
    Sheet = data.sheet_by_index(0)
    dict = {}
    Nationality = Sheet.col_values(0)
    Amount = Sheet.col_values(1)
    for i in range(1, len(Nationality)):
        dict[Nationality[i]] = Amount[i]
    return dict


def Get_Sheet_all_data_to_list():
    data = Open_Excel()
    Sheet = data.sheet_by_index(0)
    rownum = Sheet.nrows
    list = []
    for i in range(1, rownum):
        rowlist = Sheet.row_values(i)
        list.append(rowlist)
    return list


def Get_dict_to_list():
    data = Open_Excel()
    Sheet = data.sheet_by_index(0)
    rownum = Sheet.nrows  # 获取有效数据行数
    rowlist = Sheet.row_values(0)  # 把列表第一行的数据以列表对象形式放在rowlist里，将来要做字典里的键
    list = []  # 创建一个列表rowlist来接收所有的Excel表的数据
    for j in range(1, rownum):  # j=1 遍历有效的数据行，数据是从第二行开始，因为第一行是标题
        dict = {}  # 创建一个字典来接收键值对
        for i in range(len(rowlist)):  # 遍历列表rowlist的每个元素
            collist = Sheet.col_values(i)  # 创建一个collist列表来接收每一列数据对象，数据类型为list类型
            dict[rowlist[i]] = collist[j]  # 第一行的第一个值为键，列的数据也是从第一列的第二行开始
        list.append(dict)  # 把所有的字典添加到list里面
    return list
