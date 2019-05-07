#装饰器
c="这里是变量内容"

def hello():
    print("hello")
hello.__doc__="""想输入出的是,%s"""%c
print(hello.__doc__)

#使用装饰器decorate
def docstring_paramter(*sub):
    """写一个可以添加变量注释的装饰器"""
    def dec(object):
        object.__doc__=object.__doc__.format(*sub)
        return object
    return dec

#案例一：添加一个变量
@docstring_paramter("打印hello world")
def hello():
    """实现功能:{0}"""
    print(hello.__doc__)

#案例二：添加两个变量
@docstring_paramter("打印hello","打印world")
def world():
    """实现功能：{0},{1}"""
    print(world.__doc__)
hello()
world()