# coding：utf-8
import urllib
import urllib2

string = input("请输入您要查询的字符串:")
# 用fiddler抓包的结果得到的url是：http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=
# 但如果使用此url，会得到一个errorCode:500的错误
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 ",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

data = {
    "i": string,
    "to": "AUTO",
    "from": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1508029833145",
    "sign": "7df48510eed000cc4782838d7d1a55e6",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    "typoResult": "true"
}

data = urllib.urlencode(data)

request = urllib2.Request(url, data=data, headers=headers)
response = urllib2.urlopen(request)
print(response.read())
# ---------------------
# 作者：正在加载更多
# 来源：CSDN
# 原文：https://blog.csdn.net/qq_33469281/article/details/78238949
# 版权声明：本文为博主原创文章，转载请附上博文链接！
