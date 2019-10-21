# Python 中的装饰器
import time


def Waitelement(Text):
    def Outer(function):
        def Inter(*args, **kwargs):
            aaa(Text)
            function(*args, **kwargs)
            time.sleep(1)
        return Inter

    return Outer


def aaa(Text):
    print(Text)



class Test:

    @Waitelement("开始等待时间...")
    def foo(self, a=2, b=3, c=4):
        print(a + b + c)


if __name__ == '__main__':
    test = Test()
    test.foo()
